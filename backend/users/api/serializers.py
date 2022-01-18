from rest_framework import serializers
from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_photo', 'username', 'first_name', 'last_name', 'email', 'date_of_birth']


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_photo', 'username', 'date_of_birth']