from django.views.generic.base import TemplateView
from rest_framework import viewsets
from apps.profile.models import Profile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsTargetUserOrHasPerm, IsNotAllowed
from .serializers import basic, full

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profiles to be viewed
    """
    permission_classes = (IsAuthenticated, )
    queryset = Profile.objects.all().order_by('user')
    serializer_class = basic.ProfileSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

    def get_permissions(self):
        """
        - Updates require permission or ownership
        - Retrieval requires authentication
        - Deletion is not allowed
        """
        if self.action in ['update', 'partial_update']:
            return IsTargetUserOrHasPerm(),
        elif self.action in ['retrieve', 'list', 'metadata'] \
                or self.request.method in ['HEAD', 'OPTIONS']:
            return IsAuthenticated(),
        else:
            # 'delete', 'create' not allowed
            return IsNotAllowed(),

    def get_serializer_class(self):
        """
        - Expose all fields to privileged users
        - Allow users full access to their own object
        - Stripped down for everyone else
        """
        if 'profile.can_view_full_profiles_of_others' \
                in self.request.user.get_all_permissions():
            return full.ProfileSerializer
        if self.detail:
            obj = self.get_object()
            if obj.user == self.request.user:
                return full.ProfileSerializer
        return basic.ProfileSerializer