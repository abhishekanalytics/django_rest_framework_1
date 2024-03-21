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


from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError("New password and confirm password do not match.")
        return data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()