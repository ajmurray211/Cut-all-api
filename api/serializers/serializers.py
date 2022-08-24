from rest_framework import serializers
from ..models.models import Part, Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id',
            'name',
            'amountTaken',
            'dateTaken'
        )

class PartSerializer(serializers.ModelSerializer):
    drawList = WorkerSerializer(many=True, read_only=True)
    class Meta:
        model = Part
        fields = [
            'id',
            'name',
            'onHand',
            'tool',
            'drawList'
        ]