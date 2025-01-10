
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import Model
from django.utils import timezone


class User(Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="email@email.com")
    admin = models.BooleanField(default=False)


class Animals(Model):
    STATUS_CHOICES = (
        ('adoptowany', 'Adoptowany'),
        ('nie-adoptowany', 'Nie-adoptowany')
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='zdjecia', blank=True, null=True)
    animal_race = models.CharField(max_length=100)
    age = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    dodano = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20,
                             choices=STATUS_CHOICES,
                             default='Nie-adoptowany')

# Create your models here.
