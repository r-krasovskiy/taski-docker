"""Administration zone of the project."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Desplay of task section."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
