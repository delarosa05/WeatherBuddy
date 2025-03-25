from django.db import models
from datetime import datetime
from django.utils import timezone

class Measures(models.Model):    
    light_level = models.FloatField()
    pressure_level = models.FloatField()
    temperature = models.FloatField()
    humidity_level = models.FloatField() #Cambiar si la humedad se mide con porcentajes
    #raindrops = models.FloatField()
    createdAt = models.DateTimeField(default= timezone.now)

class Users(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    createdAt = models.DateField(default=timezone.now)

#Para las migraciones: python manage.py makemigrations --> python manage.py migrate 
# INSTALAR POSTGRESQL