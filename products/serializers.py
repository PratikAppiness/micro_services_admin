from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    field = '__all__'