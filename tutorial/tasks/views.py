from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from django.http import Http404
from .serializers import TasksSerializer


class TaskList(APIView):
    def get(self,request,format=None):
            tasks = Task.objects.all()
            serializer = TasksSerializer(tasks, many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        serializer = TasksSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        tasks=self.get_object(pk)
        serializer = TasksSerializer(tasks)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        tasks=self.get_object(pk)
        serializer = TasksSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        tasks=self.get_object(pk)
        tasks.delete()
        return Response({'message':'Successfully deleted'})