from rest_framework import serializers
from apps.profile.models import Profile
from apps.user.api.serializers import full
from django.contrib.auth.models import User

class SocialAccountSerializer(serializers.Serializer):
    date_joined = serializers.DateTimeField()
    last_login = serializers.DateTimeField()
    extra_data = serializers.JSONField()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # dropbox, agave, and globus are overridden by the __init__ method
    # because we need to forward the request context.
    # SocialAccountSerializer changes its fields based on permissions
    gravatar = serializers.ReadOnlyField()
    dropbox = SocialAccountSerializer(many=True)
    agave = SocialAccountSerializer(many=True)
    globus = SocialAccountSerializer(many=True)
    user = full.UserSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'institution', 'gravatar',
                  'dropbox', 'agave', 'globus', 'user',
                  'url')