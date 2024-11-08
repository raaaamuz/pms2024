from django.urls import path
from .views import CrossTabAPIView

urlpatterns = [
    path('crosstab/', CrossTabAPIView.as_view(), name='crosstab'),
]
