# urls.py

from django.urls import path
from .views import signup, user_login  # Import the user_login view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),  # Define the URL pattern for the login view

]
