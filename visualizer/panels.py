import os
from typing import Mapping, Any

import requests
from django.conf import settings
from django.template.loader import render_to_string
from wagtail.admin.panels import HelpPanel, Panel


class FhirResourceVisualizerPanel(HelpPanel):
    def __init__(self, resource_type=None, resource_id=None, collapsed_fields=None, fhir_endpoint=None, *args, **kwargs):
        assert isinstance(resource_type, str) or callable(resource_type), "resource_type can be a string or a function like \"lambda instance: instance.resource_type\""
        assert isinstance(resource_id, str) or callable(resource_id), "resource_id can not be a string or a function like \"lambda instance: instance.resource_id\""
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.collapsed_fields = collapsed_fields
        self.fhir_endpoint = fhir_endpoint or settings.FHIR_ENDPOINT

        super().__init__(*args, **kwargs)
        self.template = 'visualizer/resource_visualizer.html',

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update({
            'resource_type': self.resource_type,
            'resource_id': self.resource_id,
            'collapsed_fields': self.collapsed_fields,
            'fhir_endpoint': self.fhir_endpoint,
        })
        return kwargs

    class BoundPanel(Panel.BoundPanel):

        def render_html(self, parent_context: Mapping[str, Any] = None) -> str:

            resource_type = self.panel.resource_type(self.instance) if callable(self.panel.resource_type) else self.panel.resource_type
            resource_id = self.panel.resource_id(self.instance) if callable(self.panel.resource_id) else self.panel.resource_id

            endpoint = os.path.join(resource_type, resource_id)
            resource = requests.get(os.path.join(self.panel.fhir_endpoint, endpoint)).json()

            from visualizer.admin import ResourceAdmin
            return render_to_string(self.panel.template, {
                "collapsed_fields": self.panel.collapsed_fields,
                "html_fields": ["div"],
                "resource": resource,
                "model_url": ResourceAdmin().url_helper.get_action_url("edit", 0).rsplit("/", 2)[0]
            })
