"""API serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer."""

    class Meta:
        """Nested class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
