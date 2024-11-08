from rest_framework import serializers
from .models import Segment

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
       
        for field in self.fields:
            if field not in representation:
                representation[field] = None
        
        return representation
