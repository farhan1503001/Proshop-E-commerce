from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'