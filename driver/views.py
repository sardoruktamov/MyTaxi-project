from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Driver

class CreateDriverAPIView(APIView):
    def post(self, request):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        car_number = data['car_number']
        phone_number = data['phone_number']
        driver = Driver.objects.create(first_name=first_name, last_name=last_name,
                                       car_number=car_number, phone_number=phone_number)

        return Response("Driver is created!", status=status.HTTP_201_CREATED)