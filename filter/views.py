from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Filter
from .serializers import FilterSerializer
from user.models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class FilterViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FilterSerializer

    def get_queryset(self):
        user = self.request.user
        return Filter.objects.filter(user=user)

    def create(self, request):
        email = request.data.get('email')
        filter_name = request.data.get('filter_name')
        filters = request.data.get('filters')

        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        user_pk = user.pk

        serializer = FilterSerializer(data={'user': user_pk, 'filter_name': filter_name, 'filter_data': filters})
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getFilterNames(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            filters = Filter.objects.filter(user=user_id)
            serializer = FilterSerializer(filters, many=True)
            return Response(serializer.data)
        else:
            return Response("User not authenticated", status=403)

    @action(detail=False, methods=['delete'])
    def deleteFilterByName(self, request):
        filter_name = request.query_params.get('filter_name')
        print("DDDDDDDDDDDDDDDEEEEEEEEE",filter_name)
        if filter_name:
            try:
                user_id = request.user.id
                filter_to_delete = Filter.objects.get(user=user_id, filter_name=filter_name)
                filter_to_delete.delete()
                return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
            except Filter.DoesNotExist:
                return Response({'error': 'Filter does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Filter name not provided'}, status=status.HTTP_400_BAD_REQUEST)
