from rest_framework import serializers
from .models import Filter

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ['user','filter_name','filter_data'] # This will include all fields from the Data model

    def validate_filter_name(self, value):
        """
        Check if the filter_name already exists for the same user.
        """
        user = self.initial_data['user']
        if Filter.objects.filter(user=user, filter_name=value).exists():
            raise serializers.ValidationError("Filter with this name already exists for this user.")
        return value

    def create(self, validated_data):
        return Filter.objects.create(**validated_data)    