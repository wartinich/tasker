from rest_framework import serializers
from tasks.models import Task
from users.api.serializers import UserProfileSerializer


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'date_of_done', 'done']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user','title', 'date_of_done', 'done']


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'date_of_done', 'done']

