from rest_framework import generics
from rest_framework import permissions
from tasks.api.serializers import CreateTaskSerializer, TaskSerializer, UpdateTaskSerializer
from tasks.models import Task


class CreateTaskView(generics.CreateAPIView):
    #Create task
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListView(generics.ListAPIView):
    #User Task list
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class UpdateTaskView(generics.UpdateAPIView):
    #Update task
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer
