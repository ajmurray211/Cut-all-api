from django.db import models
from .worker import Worker

class Part(models.Model):
    name = models.CharField(max_length=200)
    onHand = models.BigIntegerField(null=True ,blank=True)
    tool = models.CharField(max_length=200, blank=True)
    workerKey = models.ForeignKey(to='api.worker', related_name='workerKey', on_delete=models.CASCADE, null=True)