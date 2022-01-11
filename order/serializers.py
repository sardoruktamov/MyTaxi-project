from django.db import models
from django.db.models import fields
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from .models import Order, AcceptOrder
from client.models import Client

class GetCustomerSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class OrderListSerializer(ModelSerializer):
    client = GetCustomerSerializer(read_only=True, many=False)
    class Meta:
        model = Order
        fields = ['client', 'created_at', 'update_at']
        ReadOnlyField = ['created_at', 'update_at']

class OrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = AcceptOrder
        fields = ['status']


class AcceptOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = AcceptOrder
        fields = '__all__'