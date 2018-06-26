from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrTargetUser, IsNotAllowed

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profiles to be viewed
    """
    permission_classes = (IsAuthenticated, )
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT']:
            return IsStaffOrTargetUser(),
        elif self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return IsAuthenticated(),
        else:
            # 'DELETE', 'POST' not allowed
            return IsNotAllowed(),


class UserProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Profile'
        return context


