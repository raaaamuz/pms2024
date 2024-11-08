from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import pandas as pd
from .models import Data, UploadedFile
from .serializers import DataSerializer, UploadedFileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import StreamingHttpResponse
import csv
from norms.utils import getNormsData

class DataViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        projects = Data.objects.all()
        serializer = DataSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print("ssssssssssssssssss")
        print(request.data)
        serialized_data = []
        for item in request.data:
            serializer = DataSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                serialized_data.append(serializer.data)
            else:
                print(f"Validation errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Data received and processed successfully', 'data': serialized_data}, status=status.HTTP_201_CREATED)

    def getField1(self, request):
        field_names = [field.name for field in Data._meta.get_fields()]
        return Response(field_names)

    def getData(self, request):
        fName = request.GET.get('fName')
        if not fName:
            return Response({"error": "Filename is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = Data.objects.filter(filename=fName)
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)

    def getProjectDetails(self, request):
        if request.user.is_authenticated:
            projDetails = UploadedFile.objects.all()
            serializer = UploadedFileSerializer(projDetails, many=True)
            return Response(serializer.data)
        return Response("User is not authenticated", status=status.HTTP_403_FORBIDDEN)
    
    def deleteProject(self, request):
        fName = request.GET.get('fName')
        uploaded_file = UploadedFile.objects.filter(filename=fName)
        if uploaded_file.exists():
            uploaded_file.delete()
            return Response({"message": f"File '{fName}' deleted successfully."}, status=status.HTTP_200_OK)
        return Response({"error": f"File '{fName}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def postFileDetails(self, request):
        if request.user.is_authenticated:
            filename = request.data.get("filename")
            if UploadedFile.objects.filter(filename=filename).exists():
                return Response({'message': 'Duplicate entry'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = UploadedFileSerializer(data={'filename': filename, 'uploaded_by': request.user.email})
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Project Entry has been created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_403_FORBIDDEN)
    
    def getField(self, request):
        field_names = [field.name for field in Data._meta.get_fields()]
        return Response(field_names)

    def getList(self, request):
        from crosstab.views import convert_keys_to_int
        field_name = request.query_params.get("question")
        filters = request.query_params.get("filter_name")
        static_filters = request.query_params.get("filters")
        column = "liking"
        top, top2, df = getNormsData(column, filters, request.user.id, static_filters)

        if convert_keys_to_int(field_name) == False:
            side_mapped = df[field_name]
        else:
            mp = convert_keys_to_int(field_name)
            dmp = {int(key): value for key, value in mp.items()}
            side_mapped = df[field_name].map(dmp)

        values = side_mapped.unique().tolist()
        values = [value for value in values if pd.notna(value)]
        
        return Response(values)

class Echo:
    def write(self, value):
        return value

class DownloadDataAPIView(APIView):
    def post(self, request, *args, **kwargs):
        filenames = request.data.get('filenames', [])
        if not filenames:
            return Response({"error": "No filenames provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Data.objects.filter(filename__filename__in=filenames)
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)

        fields = [field.name for field in Data._meta.fields if field.concrete]

        response = StreamingHttpResponse(
            self.stream_csv(writer, queryset, fields),
            content_type="text/csv"
        )
        response['Content-Disposition'] = 'attachment; filename="downloaded_data.csv"'
        return response

    def stream_csv(self, writer, queryset, fields):
        yield writer.writerow(fields)
        for obj in queryset:
            row = [getattr(obj, field) for field in fields]
            yield writer.writerow(row)
