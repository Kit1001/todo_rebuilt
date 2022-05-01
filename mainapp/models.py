from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignees = models.ManyToManyField(User, related_name='tasks', blank=True)
