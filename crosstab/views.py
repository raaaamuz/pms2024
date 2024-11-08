from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from data.models import Data
import os
import json
import pandas as pd
from filter.models import Filter
from .data_map import DataMap

class CrossTabAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = authenticate(request, email="email", password="xxx")
        print(request.user)
        if request.user.is_authenticated:
            # User is authenticated, access user credentials
            username = request.user.username
            email = request.user.email
            user_id=request.user.id
            #print(username,'x',email,'x',user_id)
        else:
            print("user not authenticated")
        if request.method == 'GET':
            
            top = request.GET.get('parameter2')
            side = request.GET.get('parameter1')
            table_type= request.GET.get('parameter4')
            filters = request.GET.getlist('parameter3')
            filter_query=''
            if filters:
            
                processed_filters = ''
                # Enclose the filter name in single quotes
                filter_name = "'" + filters[0] + "'"  # Enclose the filter name in single quotes
                filtered_filters = Filter.objects.filter(user=user_id, filter_name=filters[0])
                
                for filter_instance in filtered_filters:
                    processed_filters=filter_instance.filter_data
               
                filter_query=self.filter_to_query(processed_filters)
                filter_query=filter_query
                
                file_path = os.path.join(os.getcwd(), "crosstab", "datamap.json")
                
                
                # Create an instance of DataMap
                dmap = DataMap(file_path)
                filter_query=dmap.map_input_to_code(filter_query)


            else:
                print("No filters provided")
                processed_filters = []        

            data_entries = Data.objects.all()
            

            #if side and top:
            data_entries = data_entries.values()

            df = pd.DataFrame(data_entries)
            if filters:

                filter_condition=filter_query

                df=df.query(filter_condition)

            else:
                df=df
            #print("1xxxxxxxx",df.head())
        
        if side in df.columns:
            print("DataFrame contains ",side)
        else:
            print("DataFrame does not contain ", side)
        
        
        if convert_keys_to_int(side)==False:
            side_mapped=df[side]
            
        else:
            mp=convert_keys_to_int(side)
            dmp = {int(key): value for key, value in mp.items()}
            side_mapped = df[side].map(dmp)


        if convert_keys_to_int(top)==False:
            top_mapped=df[top]
        else:
            tmp=convert_keys_to_int(top)
            tdmp = {int(key): value for key, value in tmp.items()}
            top_mapped = df[top].map(tdmp)

        if table_type == "Percentage":
            df_tot = side_mapped.value_counts()
            side_df = side_mapped.value_counts(normalize=side)
            df1=pd.DataFrame(side_df)
            #print(df1)
            side_tot=df_tot.sum()
            cross_tab_result = pd.crosstab(side_mapped, top_mapped, normalize="columns")
            cross_tab_result.reset_index(inplace=True)
            cross_tab_result.set_index(side, inplace=True)

            merged_df = cross_tab_result.join(df1)
            print(merged_df)
            cross_tab_result = merged_df.multiply(100).round(2).astype(str) + '%'

        else:
            df_tot = side_mapped.value_counts()
            side_df = side_mapped.value_counts()
            df1=pd.DataFrame(side_df)
            #print(df1)
            side_tot=df_tot.sum()
            cross_tab_result = pd.crosstab(side_mapped, top_mapped)
            cross_tab_result.reset_index(inplace=True)
            cross_tab_result.set_index(side, inplace=True)
            cross_tab_result=cross_tab_result.join(df1)
        
        cross_tab_result_tot = pd.crosstab(side_mapped, top_mapped)

        #print("TB1",cross_tab_result)
        
        last_row_index = cross_tab_result.shape[0] - 1
        last_column_index = cross_tab_result.shape[1] - 1
        cross_tab_result.loc['Total'] = cross_tab_result_tot.sum()

        cross_tab_result.iloc[-1, last_column_index] = side_tot

        # Rename the columns to 'Total' (assuming you want to rename 'proportion' column to 'Total')
        cross_tab_result.rename(columns={"proportion": "Total"}, inplace=True)
        cross_tab_result.rename(columns={"count": "Total"}, inplace=True)

        # Ensure unique column names
        cross_tab_result.columns = [str(col) for col in cross_tab_result.columns]

        # Convert DataFrame to JSON
        cross_tab_json = cross_tab_result.to_json(orient='index')

        return JsonResponse({'cross_tab_data': cross_tab_json})
    
    def filter_to_query(self,filter_string):
        # Split the filter string by "AND"
        print(filter_string)
        conditions = filter_string.split(" (AND) ")

        # Initialize an empty list to store the query conditions
        query_conditions = []

        # Parse and construct query for each condition
        for condition in conditions:
            # Check if the condition contains "OR"
            if " OR " in condition:
                # If condition contains "OR", split and construct sub-queries
                sub_conditions = condition.split(" (OR) ")
                sub_query = " | ".join(parse_condition(sub_cond) for sub_cond in sub_conditions)
                query_conditions.append(f"({sub_query})")
            else:
                # Single condition without "OR"
                query_conditions.append(parse_condition(condition))

        # Join the query conditions with "AND" to construct the final query
        final_query = " & ".join(query_conditions)

        return final_query

    

    def post(self, request):
        # Your existing logic for processing POST requests
        # Replace this logic with your existing logic
        pass
    
def parse_condition(condition):
        key, value = condition.split(":")
        key = key.strip()
        value = value.strip()

        # Check if value contains multiple options separated by comma
        if "," in value:
            options = [f"'{option.strip()}'" for option in value.split(",")]
            return f"{key} in [{', '.join(options)}]"
        else:
            return f"{key} == '{value}'"
        
def convert_keys_to_int(field):
    # Construct the file path
    file_path = os.path.join(os.getcwd(), "crosstab", "datamap.json")
    # Initialize the formatted key dictionary
    formatted_key = {}
    
    # Read the input data from the JSON file
    with open(file_path, "r") as file:
        input_data = json.load(file)
    
    # Check if the field matches any key in the input data
    if field in input_data:
        # Retrieve the dictionary corresponding to the field
        dmap = input_data[field]
        
        # Iterate over the key-value pairs in the dictionary
        for k, v in dmap.items():
            # Check if v is a dictionary
            if isinstance(v, dict):
                # If v is a dictionary, assign it directly
                formatted_key[k] = v
            else:

                # If v is not a dictionary, assign it directly
                formatted_key[k] = v
        return formatted_key
    else:
        return False
    

