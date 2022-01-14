from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from client.models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"