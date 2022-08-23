import django


from django.db import models

class Worker(models.Model):
    name= models.CharField(max_length=30)
    amountTaken = models.BigIntegerField()
    dateTaken = models.DateField()