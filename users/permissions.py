from rest_framework import permissions


class IsAuthenticatedAndAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user.is_staff or obj.user == request.user)


class IsUnauthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated
