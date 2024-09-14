"""Config module."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API config class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
