from rest_framework import generics
from tasks.api.serializers import TaskSerializer
from tasks.models import Task


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
