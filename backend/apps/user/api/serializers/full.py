from django.contrib.auth.models import User, Group
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'groups', 'is_staff', 'is_active',
                  'date_joined', 'url')
        extra_kwargs = {
            'groups': {'lookup_field': 'pk'}
        }