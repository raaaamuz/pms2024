from django.contrib import admin
from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        'survey_id', 
        'researcher_in_charge', 
        'project_name', 
        'job_number', 
        'year', 
        'month', 
        'dp_or_scripting', 
        'dp_or_scripting', 
        'scripting_in_charge', 
        'Q1',  # Display individual question responses
        'Q2',
        'Q3',
        'Q4',
        'Q5',
        'Q6',
        'Q7',
        'Q8'
    )

admin.site.register(Survey, SurveyAdmin)
