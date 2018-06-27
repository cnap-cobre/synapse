from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def to_internal_value(self, data):
        # 400 - Bad request if unallowed fields are present
        allowed = ['csrfmiddlewaretoken']
        for field in data.keys():
            if field not in self.fields.keys() and field not in allowed:
                err = dict()
                err[field] = 'Field not allowed.'
                raise serializers.ValidationError(err)

        return super().to_internal_value(data)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user