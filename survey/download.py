import requests
import pandas as pd

# Replace this with your API endpoint
api_url = "https://4sightoperations.in/survey/survey/download/"

# Make a GET request to fetch the data from the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the JSON response
        data = response.json()
        
        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Specify the Excel file path
        output_file = "survey_data.xlsx"

        # Save the DataFrame to an Excel file
        df.to_excel(output_file, index=False)

        print(f"Data successfully saved to {output_file}")
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
