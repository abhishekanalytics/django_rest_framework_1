from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self,request,views):
        if request.method in ['GET', 'POST']:
            return True
        return False