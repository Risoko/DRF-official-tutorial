from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrSuperUserOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        return user == obj.owner or user.is_superuser

    