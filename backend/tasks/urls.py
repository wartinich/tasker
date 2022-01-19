from django.urls import path
from tasks.api.views import CreateTaskView,TaskListView, UpdateTaskView, DestroyTaskView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('delete/<int:pk>/', DestroyTaskView.as_view(), name='delete_task')
]