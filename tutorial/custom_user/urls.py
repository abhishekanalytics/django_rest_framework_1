# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# urlpatterns = [
#    path('auth/', include('rest_auth.urls')),
# ]
from django.urls import path
from .views import UserListCreateView

urlpatterns = [
    path('customusers/', UserListCreateView.as_view()), 
]
