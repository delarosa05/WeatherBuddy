from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from WeatherApp.models import *
from django.contrib.auth import authenticate
from rest_framework import viewsets
from WeatherApp.serializer import *

# Create your views here.

#Plantilla de formulario de login
def login(request):
    return render(request, "login.html") 

#Comprobacion de que el usuario existe
def checkLogin(request: HttpRequest): 
    email = request.GET["email"] #Recupera datos del input llamado email
    password = request.GET["password"]
    user = authenticate(request, username=email, password=password)  #NECESARIO ENCRIPTAR CONTRASEÑAS PARA QUE FUNCIONES
    if user is not None:
        # Login successful
        return render(request, "200login.html", {"email":email})
    else:
        return HttpResponse("error")
    

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MeasureView(viewsets.ModelViewSet):
    serializer_class = MeasureSerializer
    queryset = Measure.objects.all()   