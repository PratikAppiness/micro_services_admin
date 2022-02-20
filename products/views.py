from random import random
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.
class ProductApi(APIView):
  def list(self, request):
    """
    Write Operations
    """
    queryset      = models.Product.objects.all()
    serializer    = serializers.ProductSerializer(queryset, many=True)
    return Response({'status':status.HTTP_200_OK, 'data':serializer.data})

  def create(self, request):
    """
    Write Operations
    """
    queryset      = models.ProductCategory.objects.all()
    serializer    = serializers.ProductCategorySerializer(queryset, many=True)
    return Response({'status':status.HTTP_201_CREATED, 'data':serializer.data})

  def retrive(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.ProductCategory.objects.get(id=pk)
    serializer    = serializers.ProductCategorySerializer(queryset)
    return Response({'status':status.HTTP_302_FOUND, 'data':serializer.data})

  def update(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.ProductCategory.objects.get(id=pk)
    serializer    = serializers.ProductCategorySerializer(instance=queryset, data=request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    return Response({'status':status.HTTP_202_ACCEPTED, 'data':serializer.data})

  def destroy(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.ProductCategory.objects.get(id=pk)
    queryset.delete()
    return Response({'status':status.HTTP_204_NO_CONTENT})

class UserApi(APIView):
  def get(self, request):
    users = models.User.objects.all()
    user =  random.choice(users)
    return Response({'id': user})