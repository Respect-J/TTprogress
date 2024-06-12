from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserViewSet(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

