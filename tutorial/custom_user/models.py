from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .manager import CustomUserManager
 

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()