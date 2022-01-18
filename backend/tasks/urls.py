from django.urls import path
from tasks.api.views import TaskListView 


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks')
]