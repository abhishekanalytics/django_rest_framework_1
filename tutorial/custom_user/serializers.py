from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.EmailField(read_only=True) 
        model = CustomUser
        fields = ('id','username','email', 'first_name', 'last_name','phone_no','role')

class PartialCustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['first_name','last_name','phone_no']