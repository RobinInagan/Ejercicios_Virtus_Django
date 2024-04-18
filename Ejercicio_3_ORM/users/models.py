from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "email"
    def save(self, force_insert, force_update, using, update_fields) -> None:
        self.username = self.email.split("@")[0]
        return super().save(force_insert, force_update, using, update_fields)
    pass

