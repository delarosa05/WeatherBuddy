from django.db import models
from datetime import datetime
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=10)
    phone_number = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Measure(models.Model):    
    light_level = models.FloatField()  #verbose_name = "X" para ver este campo como "X" en el panel de administracion
    pressure_level = models.FloatField()
    temperature = models.FloatField()
    humidity_level = models.FloatField() #Cambiar si la humedad se mide con porcentajes
    #raindrops = models.FloatField()
    createdAt = models.DateTimeField(default= timezone.now)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self): #toString
        return self.light_level, self.pressure_level, self.temperature, self.humidity_level, self.createdAt
#Para las migraciones: python manage.py makemigrations --> python manage.py migrate 
