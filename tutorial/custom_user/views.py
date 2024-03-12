from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import (CustomUserSerializer,UpdateUserSerializer)
from .custom_permission import (admin_required,manager_required,employee_required) 


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
        modified_data = request.data.copy()
        serializer = UpdateUserSerializer(user, data=modified_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        users=self.get_object(pk)
        users.delete()
        return Response({'message': 'Successfully deleted'})