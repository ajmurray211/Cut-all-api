from rest_framework import serializers
from ..models.parts import Part

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            'id',
            'name',
            'onHand',
            'tool'
        )