from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client

class CreateClientAPIView(APIView):
    def post(self, request):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        phone_number = data['phone_number']
        client = Client.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number)

        return Response("Client is created!", status=status.HTTP_201_CREATED)