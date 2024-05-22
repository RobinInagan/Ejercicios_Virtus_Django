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

class Table(models.Model):
    number = models.IntegerField()
    personCapacity = models.IntegerField()

    def __str__(self) ->str:
        return str('Table Number = '+ str(self.number))

class Tables_Restaurant(models.Model):
    table = models.ForeignKey(Table,on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)


class Waiter(models.Model):
    user = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    charge = models.CharField(max_length=100)

class Waiter_Shift(models.Model):
    waiter = models.ForeignKey(Waiter,on_delete=models.DO_NOTHING)
    start_date = models.TimeField()