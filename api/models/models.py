from django.db import models

class Worker(models.Model):
    name= models.CharField(max_length=30)
    amountTaken = models.BigIntegerField(null=True)
    dateTaken = models.DateField(null=True)

    def __str__(self) -> str:
        return (self.name)

class Part(models.Model):
    name = models.CharField(max_length=200)
    onHand = models.BigIntegerField(null=True ,blank=True)
    tool = models.CharField(max_length=200, blank=True)
    drawList = models.ManyToManyField(Worker)

    def __str__(self) -> str:
        return (self.name)