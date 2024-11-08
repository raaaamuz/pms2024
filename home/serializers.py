# serializers.py

from rest_framework import serializers
from .models import Norms

class NormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Norms
        fields = '__all__'  # This will include all fields from the Norms model
