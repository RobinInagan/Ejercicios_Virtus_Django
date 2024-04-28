from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["name","address","owner"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["name","cost_per_unit","all_restaurants"]

class Products_RestaurantAdmin(admin.ModelAdmin):
    list_display=["product","restaurant"]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Products_Restaurant,Products_RestaurantAdmin)
