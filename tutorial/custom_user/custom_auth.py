from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email = request.GET.get('email')
        password = request.GET.get('password')
        
        if not email or not password:
            return None

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise AuthenticationFailed('No such user')

        if user.check_password(password):
            return (user, None)
        return None
