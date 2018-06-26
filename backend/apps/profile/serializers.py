from rest_framework import serializers

from .models import Profile
from apps.user.serializers import BasicUserSerializer, FullUserSerializer
from django.contrib.auth.models import User


class SocialAccountSerializer(serializers.Serializer):
    last_login = serializers.DateTimeField()
    date_joined = serializers.DateTimeField()
    extra_data = serializers.JSONField()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    gravatar = serializers.ReadOnlyField()
    dropbox = SocialAccountSerializer(many=True)
    agave = SocialAccountSerializer(many=True)
    globus = SocialAccountSerializer(many=True)
    user = BasicUserSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'institution', 'gravatar',
                  'dropbox', 'agave', 'globus', 'user')