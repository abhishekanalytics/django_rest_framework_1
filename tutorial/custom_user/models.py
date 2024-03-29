from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from enum import Enum
from .manager import CustomUserManager
import uuid

 
class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    EMPLOYEE = 'employee', 'Employee'

class CustomUser(AbstractUser):  
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.ADMIN)
    username=None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, blank=True)
    password_reset_done = models.BooleanField(default=False)
    reset_token_used = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()