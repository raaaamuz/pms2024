from django.urls import path
from . import views

urlpatterns = [
    path('nametest1/', views.test, name='ntest'),
]
