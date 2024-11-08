from django.urls import path
from . import views  # Assuming you have views in your survey app

urlpatterns = [
    path('create-survey/', views.create_survey, name='create-survey'),
    path('survey/<str:survey_id>/', views.get_survey_by_id, name='get-survey-by-id'),  # Add this
    path('download/', views.get_all_surveys, name='get_all_surveys'),
    path('survey/<str:survey_id>/submit-responses/', views.submit_survey_responses, name='submit-survey-responses'),
]
