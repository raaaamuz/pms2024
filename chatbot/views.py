from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai  # Import OpenAI library
from data.models import Data  # Ensure 'Data' model is correctly imported
from pathlib import Path
import json
import pandas as pd  # Import pandas for data manipulation

# Load the data map
data_map_path = Path(__file__).resolve().parent.parent / 'crosstab' / 'datamap.json'
with open(data_map_path, 'r') as f:
    data_map = json.load(f)


def fetch_data_for_columns(column_names):
    data = Data.objects.values(*column_names)
    return data

def get_mapped_columns(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        ai_response = response['choices'][0]['message']['content']
        print(f"AI Response: {ai_response}")  # Debugging print

        # Extracting the identified columns from the AI response
        mapped_columns = []
        for key, value in data_map.items():
            if key.lower() in ai_response.lower():
                mapped_columns.extend(value)
                
        return mapped_columns, ai_response
    except Exception as e:
        print(f"Error in GPT-4 Turbo processing: {str(e)}")
        return [], ""

class ChatbotAPIView(APIView):
    def post(self, request):
        user_input = request.data.get('user_input')
        if not user_input:
            return Response({"error": "User input is required"}, status=status.HTTP_400_BAD_REQUEST)

        column_names, ai_response = get_mapped_columns(user_input)
        if not column_names:
            return Response({"error": "No matching columns found"}, status=status.HTTP_404_NOT_FOUND)

        data = fetch_data_for_columns(column_names)

        # Convert fetched data to DataFrame
        df = pd.DataFrame(list(data))

        if len(column_names) != 2:
            return Response({"error": "Crosstab requires exactly two columns"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform crosstab analysis
        crosstab_result = pd.crosstab(df[column_names[0]], df[column_names[1]]).to_dict()

        return Response({"message": "Data fetched successfully", "data": crosstab_result, "ai_response": ai_response}, status=status.HTTP_200_OK)
