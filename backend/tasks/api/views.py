from rest_framework import generics
from tasks.api.serializers import TaskSerializer
from tasks.models import Task


class CreateTaskView(generics.CreateAPIView):
    #Create task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListView(generics.ListAPIView):
    #User Task list
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
