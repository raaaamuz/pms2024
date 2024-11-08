from django.urls import path,include

from .views import FilterViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('filter', FilterViewSet, basename='filter')
urlpatterns = [
     path('', include(router.urls)),
     path('filter-names/',FilterViewSet.as_view({'get':'getFilterNames'}),name='filternames'),
     path('delete-filter/', FilterViewSet.as_view({'delete': 'deleteFilterByName'}), name='delete-filter'),
]
