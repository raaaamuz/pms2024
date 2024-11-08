from django.urls import path
from django.contrib import admin
from .views import Percentile

urlpatterns = [
  
    path('percentiles/', Percentile.as_view(), name='percentiles'),
]
