from django.contrib.auth.models import User, AnonymousUser
from rest_framework import permissions, status
from rest_framework import viewsets, views, renderers
from rest_framework.response import Response

from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectAPIView(views.APIView):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]

    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        projects = request.user.projects.get_queryset()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TaskAPIView(views.APIView):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]

    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        tasks = request.user.tasks.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
