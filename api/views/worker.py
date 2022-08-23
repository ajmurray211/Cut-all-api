from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.worker import Worker
from django.shortcuts import get_object_or_404
from ..serializers.worker import WorkerSerializer

class WorkersView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        onHandDec = request.GET.get('onHandDec', None)
        onHandAce = request.GET.get('onHandAce', None)
        tool = request.GET.get('tool', None)
        if name is not None:
            worker= worker.objects.all().filter(name__contains=name)
        elif onHandDec is not  None:
            worker= worker.objects.all().order_by('-onHand').values()
        elif onHandAce is not  None:
            worker= worker.objects.all().order_by('onHand').values()
        elif tool is not  None:
            worker= worker.objects.all().filter(tool=tool)
        else:
            worker = worker.objects.all()
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
