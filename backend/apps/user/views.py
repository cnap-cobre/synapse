from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import BasicUserSerializer, FullUserSerializer, GroupSerializer
from .permissions import IsStaffOrTargetUser, IsNotAllowed


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BasicUserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        elif self.request.method in ['PATCH', 'PUT']:
            return IsStaffOrTargetUser(),
        elif self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return IsAuthenticated(),
        else:
            # 'DELETE' not allowed
            return IsNotAllowed(),


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer