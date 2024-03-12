from rest_framework.permissions import BasePermission
from .models import UserRole

class admin_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRole.ADMIN

class manager_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [UserRole.MANAGER, UserRole.ADMIN]

class employee_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [UserRole.EMPLOYEE, UserRole.ADMIN]