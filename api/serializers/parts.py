from rest_framework import serializers
from ..serializers.worker import WorkerSerializer
from ..models.parts import Part

class PartSerializer(serializers.ModelSerializer):
    workerKey = WorkerSerializer(many=True, read_only=True)
    class Meta:
        model = Part
        fields = [
            'id',
            'name',
            'onHand',
            'tool',
            'workerKey'
        ]