from rest_framework import serializers
from ..models.parts import Part

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        feilds = (
            'name',
            'onHand',
            'tool'
        )