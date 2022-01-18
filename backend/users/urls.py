from django.urls import path
from users.api.views import UserDetailView


urlpatterns = [
    path('detail/<int:id>/', UserDetailView.as_view(), name='user_detail')
]