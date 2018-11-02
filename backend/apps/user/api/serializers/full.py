from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, user):
        return user.get_full_name()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name',
                  'username', 'email', 'groups', 'is_staff',
                  'is_active', 'date_joined', 'url')
        extra_kwargs = {
            'groups': {'lookup_field': 'pk'}
        }
