from django.shortcuts import render
from rest_framework.response import Response
from WeatherApp.models import *
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from rest_framework.views import APIView
from WeatherApp.serializer import *

# Create your views here.


class UserMeasuresAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, userIdreq):
        if request.user.id != int(userIdreq):
            raise PermissionDenied("You do not have permission to access this data")
        
        measures = Measure.objects.filter(Measure.us).order_by(Measure.createdAt).first()
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, userIdreq):    
        try:
            user = Measure.objects.filter(id =userIdreq)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except (Exception):
            return Response(Exception)