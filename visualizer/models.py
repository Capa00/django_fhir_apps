from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Resource(models.Model):
    resource_type = models.CharField(_("Resource Type"), max_length=255)
    name = models.CharField(_("Name"), max_length=255, editable=False)
    #mpId = models.CharField(_("mpId"),   max_length=255)
    data = models.TextField(_("Data"), blank=True)

    class Meta:
        unique_together = ["resource_type", "name"]

    def __str__(self):
        return f"{self.name} - {self.resource_type}"

    @property
    def _resource_type(self):
        return self.resource_type

    # @property
    # def _mpId(self):
    #     return self.mpId

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # definire il resource type da data
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class ResourceType(models.Model):
    name = models.CharField(_("Resource Type"), max_length=255, unique=True)

    def __str__(self):
        return self.name
