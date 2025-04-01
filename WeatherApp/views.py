from django.http import HttpResponse
from rest_framework.response import Response
from WeatherApp.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.views import APIView
from WeatherApp.serializer import *

# Create your views here.


class UserMeasuresAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, userId):
        if request.user.id != int(userId):
            raise PermissionDenied("You do not have permission to access this data")
        
        measures = Measure.objects.filter(userId = request.user.id).order_by(Measure.createdAt).first()
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)

#Clase encargada de la gestion de usuarios, get para ver perfil y post para el registro de usuarios
class UserAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, userId):    
        try:
            reqId = request.user.id
            user = User.objects.get(id=userId)  # Asumiendo que el modelo se llama User
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return HttpResponse(e)

class UserLoginView(APIView):
        def post(self, request):
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():  
                    user = serializer.save()
                    return Response({
                    'user': UserSerializer(user).data,
                    'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
                return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
        