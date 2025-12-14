from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']