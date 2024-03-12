from rest_framework.permissions import BasePermission
from .models import UserRoleEnum

class admin_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoleEnum.ADMIN.value

class manager_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [UserRoleEnum.MANAGER.value, UserRoleEnum.Admin.value]

class employee_required(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [UserRoleEnum.employee.value, UserRoleEnum.Admin.value]