from rest_framework import serializers
from tasks.models import Task
from users.api.serializers import UserProfileSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Task
        fields = ['id', 'title', 'user', 'date', 'done']

