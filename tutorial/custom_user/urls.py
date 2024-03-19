from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import views as auth_views
from .views import (
UserListCreateView,
UserDetailView,
change_password,
PasswordResetAPIView,PasswordResetConfirmView
)


urlpatterns = [
    path('user/', UserListCreateView.as_view()), 
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('change_password/', change_password.as_view()),
    path('forgot-password/', PasswordResetAPIView.as_view(), name='forgot_password'),
    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]