import pandas as pd
from django.http import JsonResponse
from data.models import Data
import os
import json

def cross_tab(request):
    if request.method == 'GET':
        top = request.GET.get('parameter2')
        side = request.GET.get('parameter1')
        #print("xasad",request.GET.get('parameter3'))
        type= request.GET.get('parameter4')
        filt="secnew"


    data_entries = Data.objects.all()
    #print(type(data_entries),data_entries)

    if side and top:
        data_entries = data_entries.values(side, top,filt)

    df = pd.DataFrame(data_entries)
    #print(df['secnew'].value_counts())
    #df = pd.DataFrame(data_entries)
    #print(df.dtypes)
    val=[1,2,3]
    filtered_df = df[df[filt].astype(int).isin(val)]

    #print("xxxxxxxxx",len(filtered_df))
    print(df.index)
    if convert_keys_to_int(side)==False:
        side_mapped=filtered_df[side]
    else:
        side_mapped = filtered_df[side].map(convert_keys_to_int(side))
    if convert_keys_to_int(top)==False:
        top_mapped=filtered_df[top]
    else:
        top_mapped = filtered_df[top].map(convert_keys_to_int(top))

    # Create a DataFrame with all possible keys from data map
    all_keys_df = pd.DataFrame(columns=range(1, len(side_mapped) + 1))
    # Reindex side_mapped and top_mapped to fill missing values with 0
    side_mapped = side_mapped.reindex(all_keys_df.columns, fill_value=0)
    top_mapped = top_mapped.reindex(all_keys_df.columns, fill_value=0)

    # Create crosstab using reindexed side_mapped and top_mapped

    if type=="Percentage":
        cross_tab_result = pd.crosstab(side_mapped, top_mapped,normalize="columns")
        cross_tab_result = cross_tab_result.multiply(100).round(2).astype(str) + '%'
    else:
        cross_tab_result = pd.crosstab(side_mapped, top_mapped)
    
    cross_tab_result_tot = pd.crosstab(side_mapped, top_mapped)

    print("TB1",cross_tab_result)
    
    # Optionally, add a 'Total' row and column
    cross_tab_result.loc['Total'] = cross_tab_result_tot.sum()
    cross_tab_result['Total'] = cross_tab_result_tot.sum()

    print("TB2",filtered_df[side].value_counts())
    
    # Drop the first row and second column
    cross_tab_result = cross_tab_result.iloc[1:, 1:]

    # Ensure unique column names
    cross_tab_result.columns = [str(col) for col in cross_tab_result.columns]

    # Convert DataFrame to JSON
    cross_tab_json = cross_tab_result.to_json(orient='index')
    print(cross_tab_result)
    #print(cross_tab_json)
    
    return JsonResponse({'cross_tab_data': cross_tab_json})


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

