from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If read-only permissionfor all request types
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the author can edit/delete the post.
        return obj.author == request.user
