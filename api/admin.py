from django.contrib import admin
from api.models.parts import Part
from api.models.worker import Worker

# Register your models here.

admin.site.register(Part)
admin.site.register(Worker)