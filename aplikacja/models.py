
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import Model
from django.utils import timezone


class User(Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)


class Animals(Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    animal_race = models.CharField(max_length=100)
    age = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    dodano = models.DateTimeField(default=timezone.now)

# Create your models here.
