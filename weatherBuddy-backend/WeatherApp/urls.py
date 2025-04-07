from django.urls import path, include
from rest_framework import routers
from WeatherApp.views import UserAPIView, UserRegisterView, UserLoginView, UserMeasuresView

urlpatterns = [
    path('myMeasures/', UserMeasuresView.as_view(), name='myMeasures'),
    path('myProfile/', UserAPIView.as_view(), name = "my-profile"),
    path('register/', UserRegisterView.as_view(), name= "register"),
    path('login/', UserLoginView.as_view(), name="login")
]