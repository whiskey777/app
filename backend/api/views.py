from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MetalSerializer
from metals.models import Metal

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': 'api/metals'},
    ]

    return Response(routes)

@api_view(['GET'])
def getMetals(request):
    metals = Metal.objects.all()
    serializer = MetalSerializer(metals, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def metalsUpdate(request):
    
    return Response()
