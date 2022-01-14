import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer

#GET, POST
class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#GET_ID, PUT
class RetrieveClientAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

