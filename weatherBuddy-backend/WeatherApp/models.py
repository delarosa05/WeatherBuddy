from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Usa hashing
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email


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
