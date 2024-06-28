from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class ReadOnlyViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    pass


class WriteOnlyViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    pass


class UserReadViewSet(ReadOnlyViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserWriteViewSet(WriteOnlyViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileReadViewSet(ReadOnlyViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileWriteViewSet(WriteOnlyViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
