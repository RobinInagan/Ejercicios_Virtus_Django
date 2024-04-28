from django.db import models

# Imports From self Modules
from apps.User.models import Users


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(Users,on_delete = models.DO_NOTHING)

    def __str__(self) ->str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    cost_per_unit = models.IntegerField()
    all_restaurants = models.BooleanField(default=False)

    def __str__(self) ->str:
        return self.name

class Products_Restaurant(models.Model):
    product = models.ForeignKey(Product,on_delete = models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.DO_NOTHING)

