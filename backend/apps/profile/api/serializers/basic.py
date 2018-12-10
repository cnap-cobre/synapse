from rest_framework import serializers
from apps.profile.models import Profile
from apps.user.api.serializers import full, basic
from django.contrib.auth.models import User


class SocialAccountSerializer(serializers.Serializer):
    date_joined = serializers.DateTimeField()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    gravatar = serializers.ReadOnlyField()
    dropbox = SocialAccountSerializer(many=True)
    agave = SocialAccountSerializer(many=True)
    globus = SocialAccountSerializer(many=True)
    jupyter = SocialAccountSerializer(many=True)
    user = basic.UserSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'institution', 'gravatar',
                  'dropbox', 'agave', 'globus', 'jupyter', 'user',
                  'url')
