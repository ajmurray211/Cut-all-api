from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.models import Part, Worker
from django.shortcuts import get_object_or_404
from ..serializers.serializers import PartSerializer, WorkerSerializer
from django.db.models.functions import Lower

class PartsView(APIView):
    def put(self,request, *args, **kwargs):
        b = Part.objects.get(id=33)
        e = Worker.objects.get(id=request.data['drawList'][0]['id'])
        b.drawList.add(e) 
        data = PartSerializer(b, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        name = request.GET.get('name', None)
        onHandDec = request.GET.get('onHandDec', None)
        onHandAce = request.GET.get('onHandAce', None)
        tool = request.GET.get('tool', None)
        if name is not None:
            part= Part.objects.all().filter(name__contains=name)
        elif onHandDec is not  None:
            part= Part.objects.all().filter().order_by('-onHand').values()
        elif onHandAce is not  None:
            part= Part.objects.all().filter(onHandAce=onHandAce).order_by('onHand').values()
        elif tool is not  None:
            part= Part.objects.all().filter(tool=tool)
        else:
            part = Part.objects.all().filter().order_by('-name')
        data = PartSerializer(part, many=True).data
        return Response(data)
    
    def post(self, request):
        part = PartSerializer(data = request.data)
        if part.is_valid():
            part.save()
            return Response(part.data, status=status.HTTP_201_CREATED)
        else:
            return Response(part.errors, status=status.HTTP_400_BAD_REQUEST)

class PartView(APIView):
    def get(self,request, pk):
        part = get_object_or_404(Part, pk=pk)
        data = PartSerializer(part).data
        return Response(data)

    def put(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        if 'drawList' in request.data:
            drawListUpdate = Worker.objects.get(id=request.data['drawList'])
            part.drawList.add(drawListUpdate) 
        data = PartSerializer(part, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        part = get_object_or_404(Part, pk=pk)
        part.delete()
        part = Part.objects.all()
        data = PartSerializer(part, many=True).data
        return Response(data)

class WorkersView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        amountTaken = request.GET.get('amountTaken', None)
        dateTaken = request.GET.get('dateTaken', None)
        if name is not None:
            worker= Worker.objects.all().filter(name__contains=name).order_by('id')
        elif dateTaken is not  None:
            worker= Worker.objects.all().order_by('name','-dateTaken')
        elif amountTaken is not  None:
            worker= Worker.objects.all().order_by('name','amountTaken' )
        else:
            worker = Worker.objects.all().order_by('name', 'id')
        data = WorkerSerializer(worker, many=True).data
        return Response(data)
    
    def post(self, request):
        worker = WorkerSerializer(data = request.data)
        if worker.is_valid():
            worker.save()
            return Response(worker.data, status=status.HTTP_201_CREATED)
        else:
            return Response(worker.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerView(APIView):
    def get(self,request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        data = WorkerSerializer(worker).data
        return Response(data)

    def put(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        data = WorkerSerializer(worker, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        worker.delete()
        worker = Worker.objects.all()
        data = WorkerSerializer(worker, many=True).data
        return Response(data)