from django.urls import path
from .views import UserListCreateView,UserRetrieveUpdateDelete

urlpatterns = [
    path('customusers/', UserListCreateView.as_view()), 
    path('customusers/<int:pk>/', UserRetrieveUpdateDelete.as_view()),
]