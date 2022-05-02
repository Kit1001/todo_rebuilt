from django.contrib import admin

# Register your models here.
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
