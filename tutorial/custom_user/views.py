import json
import re 
from django.http import HttpResponseBadRequest,HttpResponse
from django.views.generic import TemplateView
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode
from .models import CustomUser
from django.shortcuts import render,redirect
from .serializers import (
CustomUserSerializer,
UpdateUserSerializer,
ChangePasswordSerializer,
ForgotPasswordSerializer
)
from .custom_permission import (
admin_required,
manager_required,
employee_required
) 



class UserListCreateView(APIView):
    permission_classes = [admin_required] 

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)  


class UserDetailView(APIView):
    permission_classes = [admin_required]

    def get_object(self, pk):       
        return get_object_or_404(CustomUser, pk=pk)
    
    def get(self,request,pk,format=None):
        users=self.get_object(pk)
        serializer= CustomUserSerializer(users)
        return Response(serializer.data)
  
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UpdateUserSerializer(user, data=modified_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        users=self.get_object(pk)
        users.delete()
        return Response({'message': 'Successfully deleted'})


class change_password(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                new_password = serializer.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_object_or_404(CustomUser, email=email, is_active=True)
            
            reset_url = self._generate_reset_url(request, user)
            self._send_reset_email(user.email, reset_url)
            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    def _generate_reset_url(self, request, user):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        protocol = 'https' if request.is_secure() else 'http'
        domain = request.get_host()
        return f"{protocol}://{domain}{reverse('password_reset_confirm', args=[uid, token])}"
    
    def _send_reset_email(self, email, reset_url):
        email_subject = 'Password Reset'
        email_body = render_to_string('password_reset_email.html', {'reset_url': reset_url})
        email = EmailMultiAlternatives(email_subject, '', from_email=settings.EMAIL_HOST_USER, to=[email])
        email.attach_alternative(email_body, 'text/html')
        email.send()


class PasswordResetConfirmView(TemplateView):
    template_name = 'password_reset_confirm.html'

    def post(self, request, uidb64, token):
        User = get_user_model()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid) 

        if user is not None and default_token_generator.check_token(user, token):        
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password and is_valid_password(new_password):
                user.set_password(new_password)
                user.password_reset_done = False
                user.save()
                return render(request, self.template_name, {'uidb64': uidb64, 'token': token})

            if new_password != confirm_password:
                error_message = "Password should be same "
            elif not is_valid_password(new_password):
                error_message = "Password must be at least 8 characters long"
            return HttpResponse(error_message, status=400)
        
        return HttpResponseBadRequest('Invalid user or token')

def is_valid_password(password):
    is_long_enough = len(password) >= 8
    return  is_long_enough