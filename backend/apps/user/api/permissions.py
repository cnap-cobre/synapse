from rest_framework import permissions


class IsTargetUserOrHasPerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow logged in user to change own details
        # also allows for those with the explicit model permission
        return obj == request.user or \
               request.user.has_perm('auth.can_change_user')


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
