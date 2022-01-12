from django.db import models
from django.db.models import fields
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from .models import Order, AcceptOrder, OrderStatus
from client.models import Client
from rest_framework.response import Response
from rest_framework import validators
from django.shortcuts import get_object_or_404


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

    def update(self, instance, validated_data):
        status = validated_data['status']
        accepted_status = get_object_or_404(OrderStatus, status="accepted")        
        cancelled_status = get_object_or_404(OrderStatus, status="cancelled")
        
        if instance.status == accepted_status and status == cancelled_status:
            raise validators.ValidationError({'message':"Accepted bookings cannot be canceled !!!"})
        
        return super().update(instance, validated_data)

class AcceptOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = AcceptOrder
        fields = '__all__'