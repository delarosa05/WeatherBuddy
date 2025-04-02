from rest_framework import serializers
from WeatherApp.models import Measure,User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'createdAt': {'read_only': True}  # La fecha se auto-genera
        }
        
    def create(self, validated_data): #Funcion que sirve para deserializar los datos del post
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"email": "Este email ya está registrado."})
        
        user = User.objects.create_user(
            name=validated_data['name'],
            surname= validated_data['surname'],
            email=validated_data.get('email', ''),
            password= make_password(validated_data['password'])
        )
        return user

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"

    