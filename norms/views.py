from rest_framework.views import APIView
from rest_framework.response import Response
from norms.utils import getNormsData
import pandas as pd
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from crosstab.data_map import DataMap

class Percentile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            email = request.user.email
            user_id = request.user.id
            import logging
            logger = logging.getLogger(__name__)

            # Initial debug statements
            logger.debug(f"username: {username}, email: {email}, user_id: {user_id}")

            # Assigning values to variables
            column = request.GET.get("normsVar")
            filters = request.GET.get("filter_name")
            static_filters = request.GET.get("filters")
            question = request.GET.get("question", "clientname")

            # Logging after variable assignment
            logger.debug(f"column: {column}, filters: {filters}, static_filters: {static_filters}")

            # Fetching data and logging top data
            top, top2, df = getNormsData(column, filters, user_id, static_filters)

            tot_project = len(df['jobno'].unique())
            df_full = df.groupby(['productcode', 'projectname']).size()

            nop = df['productcode'].nunique()
            sample = len(df['productcode'])
            df_full_df = df_full.reset_index()

            top_data = top.groupby(['productcode', 'projectname']).size()
            top_data_df = top_data.reset_index()
            merged_df_top = pd.merge(top_data_df, df_full_df, on=['productcode', 'projectname'])
            merged_df_top['score'] = ((merged_df_top['0_x'] / merged_df_top['0_y']) * 100).round()

            top2_data = top2.groupby(['productcode', 'projectname']).size()
            top2_data_df = top2_data.reset_index()
            merged_df_top2 = pd.merge(top2_data_df, df_full_df, on=['productcode', 'projectname'])
            merged_df_top2['score'] = ((merged_df_top2['0_x'] / merged_df_top2['0_y']) * 100).round()

            # Handling NaN values
            merged_df_top['score'].fillna(0, inplace=True)
            merged_df_top2['score'].fillna(0, inplace=True)
            df[column].fillna(0, inplace=True)

            # Calculating percentiles and logging results
            top_percentile = self.percentile_calc(merged_df_top['score'])
            top2_percentile = self.percentile_calc(merged_df_top2['score'])
            logger.debug(f"top percentile: {top_percentile}, top2 percentile: {top2_percentile}")

            header = ['10 percentile', '20 percentile', '30 percentile', '40 percentile', '50 percentile', '60 percentile', '70 percentile', '80 percentile', '90 percentile']
            mean_value = df[column].mean()
            mean_percntile = self.mean_calc(df[column])

            return Response({
                "Headers": header,
                "Top Box": top_percentile,
                "Top 2 Box": top2_percentile,
                "Mean Value": mean_value,
                "Mean": mean_percntile,
                "Samples considered": sample,
                "Number of products": nop,
                "Number of projects": tot_project
            })
        else:
            return Response({"Authentication Failed": "User not authenticated"})

    def percentile_calc(self, df):
        percentiles = df.quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        return percentiles.round()

    def mean_calc(self, df):
        percentiles = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        mean_for_percentiles = {}
        for percentile in percentiles:
            percentile_cut = df[df <= df.quantile(percentile)]
            mean_for_percentiles[f'{int(percentile * 100)}th Percentile'] = percentile_cut.mean()

        mean_for_percentiles_series = pd.Series(mean_for_percentiles)
        return mean_for_percentiles_series.round(2)
