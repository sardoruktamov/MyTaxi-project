from django.db import models
from django.db.models import fields
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from .models import Driver


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'car_number', 'phone_number']
        ReadOnlyField = ['start_time']