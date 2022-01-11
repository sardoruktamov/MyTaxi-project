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

class FilterOrderAPIView(generics.ListAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = OrderListSerializer

    def filter_queryset(self, queryset):
        client = get_object_or_404(Client,id=self.kwargs['pk'])
        if 'from' in self.request.GET and 'to' in self.request.GET:
            from1 = self.request.GET['from']
            to1 = self.request.GET['to']

            from2 = (str(from1).split('/'))  #['5', '01', '2022']
            to2 = (str(to1).split('/'))

            from_date = datetime.datetime(int(from2[2]),int(from2[1]),int(from2[0]))  #2022-01-05 00:00:00
            to_date = datetime.datetime(int(to2[2]),int(to2[1]),int(to2[0]))
            queryset = AcceptOrder.objects.filter(client=client,update_at__range=(from_date, to_date))
            return super().filter_queryset(queryset)
        else:
            queryset = Order.objects.filter(client=client)
            return super().filter_queryset(queryset)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class OrderStatusUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = OrderUpdateSerializer