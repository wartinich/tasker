from django.urls import path
from users.api.views import UserDetailView, UpdateUserView


urlpatterns = [
    path('detail/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('update/<int:id>/', UpdateUserView.as_view(), name='user_update')
]