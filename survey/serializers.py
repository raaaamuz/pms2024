from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'survey_id', 
            'researcher_in_charge', 
            'project_name', 
            'job_number', 
            'year', 
            'month', 
            'dp_or_scripting', 
            'scripting_in_charge', 
            'dp_in_charge',
            'Q1',
            'Q2',
            'Q3',
            'Q4',
            'Q5',
            'Q6',
            'Q7',
            'Q8'
        ]
