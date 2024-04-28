from rest_framework import serializers
from .models import *

class RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Restaurant
        fields="__all__"