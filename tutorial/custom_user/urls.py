from django.urls import path
from .views import UserListCreateView,UserDetailView

urlpatterns = [
    path('user/', UserListCreateView.as_view()), 
    path('user/<int:pk>/', UserDetailView.as_view()),
]