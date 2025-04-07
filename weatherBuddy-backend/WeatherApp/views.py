from django.http import HttpResponse
from rest_framework.response import Response
from WeatherApp.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from WeatherApp.serializer import *
from django.contrib.auth import authenticate

# Create your views here.


class UserMeasuresView(generics.ListAPIView):
    serializer_class = MeasureSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Aquí obtienes al usuario autenticado
            user = request.user  # Esto asegura que el usuario autenticado sea el que está haciendo la solicitud

            # Filtra las medidas por el usuario
            measures = Measure.objects.filter(userId=user).order_by('-createdAt')[:1]  # Muestra la medida más reciente

            # Serializa las medidas
            serializer = MeasureSerializer(measures, many=True)

            # Devuelve las medidas serializadas como respuesta
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Clase encargada de la gestion de usuarios, get para ver perfil y post para el registro de usuarios
class UserAPIView(APIView): #MODIFICAR
    permission_classes = [IsAuthenticated]
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

class UserRegisterView(APIView): #MODIFICAR
        def post(self, request):
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():  
                    user.userId = request.user.id
                    user = serializer.save()
                    return HttpResponse({
                    'user': UserSerializer(user).data,
                    'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
                return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
        
class UserLoginView(APIView): #HECHO
    def post(self, request):
        #print(request.data) usado para depurar
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'message': 'Login exitoso',
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)