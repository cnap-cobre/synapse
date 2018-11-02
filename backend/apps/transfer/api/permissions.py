from rest_framework import permissions


class IsTargetUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details,
        #   allows staff to view all records
        return obj.user == request.user


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
