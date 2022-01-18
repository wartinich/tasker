from users.api.serializers import UserProfileSerializer
from rest_framework import generics
from users.models import User


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    # def queryset(self):
    #     return User.objects.filter(id=self.request.user.id)

    lookup_field = 'id'