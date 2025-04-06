from django.urls import path, include
from rest_framework import routers
from WeatherApp.views import UserMeasuresAPIView, UserAPIView, UserRegisterView, UserLoginView

urlpatterns = [
    path('myMeasures/', UserMeasuresAPIView.as_view(), name='my-measures'),
    path('myProfile/', UserAPIView.as_view(), name = "my-profile"),
    path('register/', UserRegisterView.as_view(), name= "register"),
    path('login/', UserLoginView.as_view(), name="login")
]