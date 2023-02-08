from django.apps import AppConfig


class EditableAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "editable_admin"
