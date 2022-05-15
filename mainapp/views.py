from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets, renderers

import calendar

from rest_framework.response import Response

from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        result = User.objects.get(id=self.request.user.id).projects.all()
        return result


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        result = User.objects.get(id=self.request.user.id).tasks.all()
        return result

