from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsManagerOrEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['manager', 'employee']

class IsOwnerOrAdminOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'manager']:
            return True
        if request.user.role == 'manager' and obj.employee == request.user:
            return True
        return request.user.role == 'employee' and obj.employee == request.user

