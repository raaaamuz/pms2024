# from django.http import JsonResponse
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Projects
# from .serializers import ProjectSerializer
# from rest_framework.decorators import action

# def home(request):
#     return JsonResponse({"message": "Hi Rama!"})

# @action(detail=False, methods=['post'])
# class ProjectsViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             project_no = serializer.validated_data.get('project_no')
#             if Projects.objects.filter(project_no=project_no).exists():
#                 return Response({'error': 'Project number already exists.'}, status=status.HTTP_400_BAD_REQUEST)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # views.py
#     #from django.http import JsonResponse

#     def upload_excel(self, request):
#         if request.method == 'POST':
#             excel_data = request.POST.get('excelData')
#             # Process and save excel_data to the database
#             return JsonResponse({'message': 'Excel data uploaded successfully'})
#         else:
#             return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.core.files.uploadedfile import InMemoryUploadedFile
import pandas as pd
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Hi Rama!"})

def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excelFile')
        if isinstance(excel_file, InMemoryUploadedFile):
            # Read the Excel file using pandas or any other library
            excel_data = pd.read_excel(excel_file)
            # Process and save excel_data to the database
            # Example:
            # for index, row in excel_data.iterrows():
            #     project_name = row['Project Name']
            #     project_no = row['Project Number']
            #     year = row['Year']
            #     project = Projects.objects.create(project_name=project_name, project_no=project_no, year=year)
            return JsonResponse({'message': 'Excel data uploaded and processed successfully'})
        else:
            return JsonResponse({'error': 'No file was uploaded'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
