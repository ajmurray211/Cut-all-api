from rest_framework import serializers
from ..models.worker import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id',
            'name',
            'amountTaken',
            'dateTaken'
        )