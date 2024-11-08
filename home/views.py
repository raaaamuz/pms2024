from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Norms
from .serializers import NormsSerializer

class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        # Retrieve all projects from the database
        projects = Norms.objects.all()
        
        # Serialize the projects
        serializer = NormsSerializer(projects, many=True)
        
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        #print("Xxxxxxxxx")
        try:
            data = request.data
            serialized_data = []

            print("Received data:", data)

            for item in data:
                serializer = NormsSerializer(data=item)

                print("Serialized data:", serializer.initial_data)

                if serializer.is_valid():
                    # Save the item to the database
                    serializer.save()

                    print("Saved data:", serializer.data)

                    # Append the serialized data to the list
                    serialized_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Data received and processed successfully', 'data': serialized_data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
