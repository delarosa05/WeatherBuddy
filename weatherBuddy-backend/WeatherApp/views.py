from django.http import HttpResponse
from rest_framework.response import Response
from WeatherApp.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from WeatherApp.serializer import *
from django.contrib.auth import authenticate

# Create your views here.


class UserMeasuresAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, userId):
        if request.user.id != int(userId):
            return Response(status=403, data="You do not have permission")
        else:
            measures = Measure.objects.filter(userId = request.user.id).order_by(Measure.createdAt).first()
            serializer = MeasureSerializer(measures, many=True)
            return Response(serializer.data)

#Clase encargada de la gestion de usuarios, get para ver perfil y post para el registro de usuarios
class UserAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):    
        try:
            reqId = request.user.id
            if user.userId == reqId:
                user = User.objects.get(id=reqId)  # Asumiendo que el modelo se llama User
                serializer = UserSerializer(user)
                return Response(data=serializer.data)
            else:
                 return Response(status=403, data="You do not have permission")
        except Exception as e:
            return HttpResponse(e)

class UserRegisterView(APIView):
        def post(self, request):
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():  
                    user.userId = request.user.id
                    user = serializer.save()
                    return Response({
                    'user': UserSerializer(user).data,
                    'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
                return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
        
class UserLoginView(APIView):
      def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.username,
                'message': 'Login exitoso',
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )