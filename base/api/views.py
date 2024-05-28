# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Server
from .serializers import ServerSerializer


# ['GET', 'PUT', 'POST'] can be added
@api_view(['GET']) 
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/servers',
        'GET /api/servers/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getServers(request):
    servers = Server.objects.all()
    serializer = ServerSerializer(servers, many=True) #many for multiple values in the list
    return Response(serializer.data)

@api_view(['GET'])
def getSingleServer(request, pk):
    server = Server.objects.get(id=pk)
    serializer = ServerSerializer(server, many=False)
    return Response(serializer.data)
