from django.urls import path, include
from rest_framework import routers
from WeatherApp.views import MeasureView,UserView

#api versioning
router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'measures', MeasureView)

urlpatterns = [
    path('api/v1', include(router.urls))
]