import random

from products.producer import publish
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.
class ProductApi(APIView):
  def get(self, request):
    """
    Write Operations
    """
    queryset      = models.Product.objects.all()
    serializer    = serializers.ProductSerializer(queryset, many=True)
    return Response({'status':status.HTTP_200_OK, 'data':serializer.data})

  def post(self, request):
    """
    Write Operations
    """
    serializer    = serializers.ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    publish('Product Created', serializer.data)
    return Response({'status':status.HTTP_201_CREATED, 'data':serializer.data})


class ProductApiSingle(APIView):
  def get(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.Product.objects.get(id=pk)
    serializer    = serializers.ProductSerializer(queryset)
    return Response({'status':status.HTTP_302_FOUND, 'data':serializer.data})

  def put(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.Product.objects.get(id=pk)
    serializer    = serializers.ProductSerializer(instance=queryset, data=request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    publish('Product Updated', serializer.data)
    return Response({'status':status.HTTP_202_ACCEPTED, 'data':serializer.data})

  def delete(self, request, pk=None):
    """
    Write Operations
    """
    queryset      = models.Product.objects.get(id=pk)
    queryset.delete()
    publish('Product Deleted', pk)
    return Response({'status':status.HTTP_204_NO_CONTENT})

class UserApi(APIView):
  def get(self, request):
    users = models.User.objects.all().values_list('id',flat=True)
    user =  random.choice(users)
    return Response({'id': user})