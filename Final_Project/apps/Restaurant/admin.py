from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["name","address","owner"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["name","cost_per_unit","all_restaurants"]

class Products_RestaurantAdmin(admin.ModelAdmin):
    list_display=["product","restaurant"]

class TableAdmin(admin.ModelAdmin):
    list_display =["number","personCapacity"]

class Tables_RestaurantAdmin(admin.ModelAdmin):
    list_display =["table","restaurant"]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Products_Restaurant,Products_RestaurantAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Tables_Restaurant,Tables_RestaurantAdmin)