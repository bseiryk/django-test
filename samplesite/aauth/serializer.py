from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone')