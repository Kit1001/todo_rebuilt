from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets, renderers
from rest_framework.response import Response

from .models import Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.GenericViewSet):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()

    def list(self, request):
        projects = request.user.projects.get_queryset()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.GenericViewSet):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()

    def list(self, request):
        tasks = request.user.tasks.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
