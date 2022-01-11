from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Order, AcceptOrder, OrderStatus
from client.models import Client
from driver.models import Driver
from .serializers import OrderListSerializer
from rest_framework.generics import ListAPIView

#client tomonidan driver zakas qilish
class CreateOrderAPIView(APIView):
    def post(self, request):
        data = request.data
        client = data['client']
        get_client = Client.objects.get(id=client)
        order = Order.objects.create(client=get_client)
        return Response("Order is created!", status=status.HTTP_201_CREATED)

#zakas holatining nazorat qismi  statuses: created, cancelled, accepted and finished
class AcceptOrderAPIView(APIView):
    def post(self, request):
        data = request.data
        driver = data['driver']
        client = data['client']
        status = data['status']

        get_driver = Driver.objects.get(id=driver)
        get_client = Client.objects.get(id=client)
        get_status = OrderStatus.objects.get(id=status)

        print(get_driver)
        print(get_client)
        print(get_status)
        accepted_order = AcceptOrder.objects.create(driver=get_driver, client=get_client, status=get_status)
        
        return Response("AcceptOrder is accepted")

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer