from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user and request.auth

