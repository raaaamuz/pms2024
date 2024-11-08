from django.urls import path
from .views import create_or_update_segment, get_input_values, get_project_names

urlpatterns = [
    path('segments/', create_or_update_segment, name='create_segment'),
    path('project-names/', get_project_names, name='project-names'),
    path('segments/<str:project_name>/', get_input_values, name='get_input_values'),
]