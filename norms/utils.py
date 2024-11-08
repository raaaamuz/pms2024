
from filter.filter_logic import FilterLogics
from filter.models import Filter
import pandas as pd
import os
from data.models import Data
from crosstab.data_map import DataMap

def getNormsData(column=None,filters=None,user_id=None,static_filter=None):
        import os
        if filters or static_filter:
            
            processed_filters = ''
            # Enclose the filter name in single quotes
            if filters:
                filter_name = "'" + filters[0] + "'"  # Enclose the filter name in single quotes
            else:
                filter_name=""
            filtered_filters = Filter.objects.filter(user=user_id, filter_name=filters)
            
            for filter_instance in filtered_filters:
                processed_filters=filter_instance.filter_data
            
            if static_filter:
                if processed_filters:
                    processed_filters=processed_filters+" (AND) "+ static_filter
                else:
                    processed_filters=static_filter
                    
            filter_query=filter_to_query(processed_filters)
            file_path = os.path.join(os.getcwd(), "crosstab", "datamap.json")

            # Create an instance of DataMap
            dmap = DataMap(file_path)
            filter_query=dmap.map_input_to_code(filter_query)

        else:
            print("No filters provided")
            processed_filters = []        

        data_entries = Data.objects.all()
        data_entries = data_entries.values()

        df = pd.DataFrame(data_entries)
        if filters or static_filter:
            filter_condition=filter_query
            df=df.query(filter_condition)
        else:
            df=df
    
        df_full=df
        
        # Check if the column is present in the DataFrame
        if column not in df.columns:
            print(f"Column '{column}' not found in DataFrame.")
            return
        
        # Filter condition 1
        top2_scale_9_condition = ((df['scaleproductattributes'] == '9-point scale') & 
                    ((df[column] == 8) | (df[column] == 9)))

        # Filter condition 2
        top2_scale_7_condition = ((df['scaleproductattributes'] == '7-point scale') & 
                    ((df[column] == 6) | (df[column] == 7)))
        
        # Filter condition 2
        top2_scale_5_condition = ((df['scaleproductattributes'] == '5-point scale') & 
                    ((df[column] == 4) | (df[column] == 5)))

        # Filter condition 1
        top_scale_9_condition = ((df['scaleproductattributes'] == '9-point scale') & 
                    ( (df[column] == 9)))

        # Filter condition 2
        top_scale_7_condition = ((df['scaleproductattributes'] == '7-point scale') & 
                    ((df[column] == 7)))
        # Filter condition 2
        top_scale_5_condition = ((df['scaleproductattributes'] == '5-point scale') & 
                    ((df[column] == 5)))

        # Apply the filters
        df_top2 = df[top2_scale_9_condition | top2_scale_7_condition|top2_scale_5_condition]
        df_top = df[top_scale_9_condition | top_scale_7_condition|top_scale_5_condition]

        return df_top, df_top2,df_full

def filter_to_query(filter_string):
        # Split the filter string by "AND"
        conditions = filter_string.split(" (AND) ")

        # Initialize an empty list to store the query conditions
        query_conditions = []

        # Parse and construct query for each condition
        for condition in conditions:
            # Check if the condition contains "OR"
            if " (OR) " in condition:
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

def parse_condition(condition):
    #print("conndition:::::::",condition)
    key, value = condition.split(":")
    key = key.strip()
    value = value.strip()
    con=''
    # Check if value contains multiple options separated by comma
    if "," in value:
        options = [f"'{option.strip()}'" for option in value.split(",")]
        con=f"{key} in [{', '.join(options)}]"
        #print ("xxxxxxxxxxxxxxxx",x)
        return con
    else:
        con=f"{key} == '{value}'"
        #print ("sssssssssssssssss",x)
        return con