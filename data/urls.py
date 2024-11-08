from django.urls import path, include
from .views import DataViewSet,DownloadDataAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('data', DataViewSet, basename='data')  # Specify the basename here
urlpatterns = [
    path('', include(router.urls)),
    path('fields/', DataViewSet.as_view({'get': 'getField'}), name='get_fields'),
    path('getdata/', DataViewSet.as_view({'get': 'getData'}), name='get_data'),
    path('option-list/', DataViewSet.as_view({'get': 'getList'}), name='get_list'),
    path('column-data/', DataViewSet.as_view({'get': 'get_column_data'}), name='get_column_data'),
    path('getPrDetails/', DataViewSet.as_view({'get': 'getProjectDetails'}), name='get_project_list'),
    path('file-details/', DataViewSet.as_view({'post': 'postFileDetails'}), name='post_list'),
    path('deleteProject/', DataViewSet.as_view({'delete': 'deleteProject'}), name='delete_project'),
    path('download_data/', DownloadDataAPIView.as_view(), name='download-data-api'),
]
