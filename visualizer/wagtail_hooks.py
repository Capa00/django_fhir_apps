import json
import os

import requests
from wagtail import hooks
from django.utils.translation import gettext as _

from editable_admin.wagtail_hooks import ListedBulkAction
from .models import ResourceType, Resource
from django.conf import settings


@hooks.register("register_bulk_action")
class UpdateResourcesBulkAction(ListedBulkAction):
    display_name = _("Update Resource")
    aria_label = _("Update all Resources")
    action_type = "update_resources"
    template_name = "visualizer/admin/confirm_update_action.html"
    models = [ResourceType]

    def __init__(self, *args, **kwargs):
        from .admin import ResourceTypeAdmin
        super().__init__(*args, **kwargs)
        self.next_url = ResourceTypeAdmin().url_helper.get_action_url('index')

    @classmethod
    def _load_from_server(cls, resource_type):
        next_page = os.path.join(settings.FHIR_ENDPOINT, resource_type)

        while next_page:
            response = requests.get(next_page)

            if response.status_code == 200:
                json_data = response.json()
                for entry in json_data['entry']:
                    resource = entry["resource"]
                    default_values = {
                        "resource_type": resource['resourceType'],
                        "name": resource['id']
                    }
                    Resource.objects.update_or_create(
                        **default_values,
                        defaults={
                            **default_values,
                            "data": json.dumps(resource)
                        }
                    )
                try:
                    next_page = next(x['url'] for x in json_data["link"] if x['relation'] == 'next')
                except StopIteration:
                    next_page = None

            else: raise Exception()



    @classmethod
    def execute_action(cls, objects, **kwargs):
        objects[0]._meta.model.objects.all().delete()
        for obj in objects:
            cls._load_from_server(obj.name)

        return len(objects), 0  # return the count of updated objects
