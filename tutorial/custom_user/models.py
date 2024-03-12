from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from enum import Enum
from .manager import CustomUserManager
 
class UserRoleEnum(Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    EMPLOYEE = 'employee'

class CustomUser(AbstractUser):  
    ROLES = [
        (role.value, role.name) for role in UserRoleEnum
        ]
    role = models.CharField(max_length=10, choices=ROLES, default=UserRoleEnum.ADMIN.value)
    username=None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()