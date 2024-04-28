from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["name","address","owner"]


admin.site.register(Restaurant,RestaurantAdmin)
