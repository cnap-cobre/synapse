from rest_framework import permissions


class IsTargetUserOrHasPerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details,
        # allows staff to view all records
        return obj.user == request.user or \
               request.user.has_perm('profile.can_change_profile')


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
