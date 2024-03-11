from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404
from .custom_permission import IsAdmin, IsManagerOrEmployee, IsOwnerOrAdminOrManager


class UserListCreateView(APIView):
    permission_classes=[IsAdmin]
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

    def get_object(self, pk):       
        return get_object_or_404(CustomUser, pk=pk)
    
    def get(self,request,pk,format=None):
        users=self.get_object(pk)
        serializer= CustomUserSerializer(users)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        user = self.get_object(pk)   
        modified_data = request.data.copy()     
        modified_email = modified_data.pop('email', None)
        serializer = CustomUserSerializer(user, data=modified_data, partial=True)     
        serializer.is_valid(raise_exception=True)
        if modified_email is not None:
            serializer.validated_data['email'] = user.email
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        users=self.get_object(pk)
        users.delete()
        return Response({'message': 'Successfully deleted'})