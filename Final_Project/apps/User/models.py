from django.db import models

from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    REQUIRED_FIELDS = ["email","FirstName","SecondName"]
    
    FirstName = models.CharField(max_length=50,default="")
    SecondName = models.CharField(max_length=50,default="")

    def save(self, *args,**kwargs) -> None:
        self.username = self.email.split('@')[0]
        return super().save(*args,**kwargs)
