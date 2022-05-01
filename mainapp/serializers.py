from django.contrib.auth.models import User
from rest_framework import serializers

from mainapp.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # projects = ProjectSerializer(many=True)
    # tasks = TaskSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'projects', 'tasks']
