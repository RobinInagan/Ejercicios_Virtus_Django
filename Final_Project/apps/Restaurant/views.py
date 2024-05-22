from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
#Self Modules
from .models import *
from .serializers import *

class RestaurantViewSet(ModelViewSet):    
        queryset = Restaurant.objects.all()
        serializer_class = RestaurantSerializerModel


class ProductViewSet(ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProdcutsSerializerModel

class Products_RestaurantViewSet(ModelViewSet):
        queryset = Products_Restaurant.objects.all()
        serializer_class = Products_RestaurantSerializerModel

class TableViewSet(ModelViewSet):
        queryset = Table.objects.all()
        serializer_class = TablesSerializerModel

class Tables_RestaurantViewSet(ModelViewSet):
        queryset = Tables_Restaurant.objects.all()
        serializer_class = Tables_RestaurantSerializerModel

class WaiterViewSet(ModelViewSet):
        queryset = Waiter.objects.all()
        serializer_class = WaiterSerializerModel
