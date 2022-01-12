from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from .models import Order, AcceptOrder, OrderStatus
from client.models import Client
from driver.models import Driver
from .serializers import OrderListSerializer, OrderUpdateSerializer, AcceptOrderCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
import datetime

#client tomonidan driver zakas qilish
class CreateOrderAPIView(APIView):
    def post(self, request):
        data = request.data
        client = data['client']
        get_client = Client.objects.get(id=client)
        order = Order.objects.create(client=get_client)
        return Response("Order is created!", status=status.HTTP_201_CREATED)

#zakas holatining nazorat qismi  statuses: created, cancelled, accepted and finished
class AcceptOrderAPIView(generics.CreateAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = AcceptOrderCreateSerializer
    def post(self, request):

        data = request.data
        driver = data['driver']
        client = data['client']
        status = data['status']

        get_driver = Driver.objects.get(id=driver)
        get_client = Client.objects.get(id=client)
        get_status = OrderStatus.objects.get(id=status)

        accepted_order = AcceptOrder.objects.create(driver=get_driver, client=get_client, status=get_status)
        serializer = AcceptOrderCreateSerializer(accepted_order, read_only=True)
        
        return Response({"status":"create accept"})

#GET- filter by client
class FilterOrderAPIView(generics.ListAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = OrderListSerializer

    def filter_queryset(self, queryset):
        client = get_object_or_404(Client,id=self.kwargs['pk'])
        if 'from' in self.request.GET and 'to' in self.request.GET:
            from_str = self.request.GET['from']                 #  2022-01-12
            to_str = self.request.GET['to']

            from_date =  datetime.datetime.strptime(from_str, "%Y-%m-%d")  #strint tipli ma'lumotni date tipiga aylantirish
            to_date = datetime.datetime.strptime(to_str, "%Y-%m-%d")

            queryset = AcceptOrder.objects.filter(client=client,update_at__range=(from_date, to_date))
            return super().filter_queryset(queryset)
        else:
            queryset = Order.objects.filter(client=client)
            return super().filter_queryset(queryset)

#GET-order
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

#PUT-status
class OrderStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = OrderUpdateSerializer

