from rest_framework import serializers
from user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'user_photo', 'username', 'first_name', 'last_name', 'email', 'date_of_birth']