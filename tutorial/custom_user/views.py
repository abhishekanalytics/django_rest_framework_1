# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import CustomUser
# from .serializers import CustomUserSerializer

# class UserListCreateView(APIView):
#     # permission_classes = [IsAuthenticated]  

#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = CustomUserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)  
#         return Response(serializer.errors, status=400)  