from django.contrib.auth.models import User
from rest_framework import serializers

from .basic import GroupSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'groups', 'is_staff', 'is_active',
                  'date_joined', 'url')