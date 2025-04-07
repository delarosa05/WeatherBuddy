from django.contrib.auth.backends import ModelBackend
from WeatherApp.models import User  # Ajusta el import según tu estructura

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get('email', username)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
