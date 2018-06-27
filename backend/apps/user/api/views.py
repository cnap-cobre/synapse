from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import full, basic, anon_create
from .permissions import IsTargetUserOrHasPerm, IsNotAllowed


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = basic.UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_permissions(self):
        """
        - Anyone can create a user and view available methods
        - Updates require permission or ownership
        - Retrieval requires authentication
        - Deletion is not allowed
        """
        if self.action in ['create', 'metadata'] \
                or self.request.method in ['OPTIONS']:
            return AllowAny(),
        elif self.action in ['update', 'partial_update']:
            return IsTargetUserOrHasPerm(),
        elif self.action in ['retrieve', 'list'] \
                or self.request.method in ['HEAD']:
            return IsAuthenticated(),
        else:
            # 'delete' not allowed
            return IsNotAllowed(),

    def get_serializer_class(self):
        """
        - Limit signup fields for anonymous
        - Expose all fields to privileged users
        - Limit signup fields for non-privileged users
        - Stripped down for everyone else
        """
        if self.request.user.is_anonymous:
            return anon_create.UserSerializer
        elif 'profile.can_view_full_profiles_of_others' \
                in self.request.user.get_all_permissions():
            return full.UserSerializer
        elif self.action == 'create':
            return anon_create.UserSerializer
        return basic.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = full.GroupSerializer