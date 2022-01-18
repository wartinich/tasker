from users.api.serializers import UserProfileSerializer
from rest_framework import generics


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def queryset(self):
        return User.objects.filter(id=self.request.user.id)

    lookup_field = 'id'