from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.parts import Part
from django.shortcuts import get_object_or_404
from ..serializers.parts import PartSerializer

class PartsView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        onHand = request.GET.get('onHand', None)
        tool = request.GET.get('tool', None)
        if name is not None:
            part= Part.objects.all().filter(name__contains=name)
        elif onHand is not  None:
            part= Part.objects.all().filter(onHand=onHand)
        elif tool is not  None:
            part= Part.objects.all().filter(tool=tool)
        else:
            part = Part.objects.all()
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
