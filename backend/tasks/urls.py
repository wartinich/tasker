from django.urls import path
from tasks.api.views import CreateTaskView,TaskListView, UpdateTaskView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
    path('update/<int:id>/', UpdateTaskView.as_view(), name='update_task')
]