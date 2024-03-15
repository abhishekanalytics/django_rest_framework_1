from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.EmailField(read_only=True) 
        model = CustomUser
        fields = ('id','username','email', 'first_name', 'last_name','phone_no','role')

class UpdateUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['first_name','last_name','phone_no']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
