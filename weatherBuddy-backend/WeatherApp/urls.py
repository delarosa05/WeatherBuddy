from django.urls import path, include
from rest_framework import routers
from WeatherApp.views import UserMeasuresAPIView, UserAPIView, UserLoginView


urlpatterns = [
    path('measures/<int:userId>/', UserMeasuresAPIView.as_view(), name='user-measures'),
    path('users/<int:userId>/', UserAPIView.as_view(), name = "users"),
    path('register/', UserLoginView.as_view(), name= "register")
]