from django.urls import path
from .views import UserListCreateView,UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('user/', UserListCreateView.as_view()), 
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]