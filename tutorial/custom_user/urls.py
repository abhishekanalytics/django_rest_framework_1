from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import views as auth_views
from .views import UserListCreateView,UserDetailView
from .views import (
change_password,
PasswordResetAPIView
)
from .views import (
PasswordResetAPIView,
change_password
)


urlpatterns = [
    path('user/', UserListCreateView.as_view()), 
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('change_password/', change_password.as_view()),
    path('forgot-password/', PasswordResetAPIView.as_view(), name='forgot_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  
]