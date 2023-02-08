import os
from typing import Mapping, Any

import requests
from django.template.loader import render_to_string
from wagtail.admin.panels import HelpPanel, Panel
from django.conf import settings


class JsonVisualizerPanel(HelpPanel):
    def __init__(self, json_dict=None, collapsed_fields=None, *args, **kwargs):
        assert isinstance(json_dict, dict) or callable(json_dict), "resource_type can be a string or a function like > lambda instance: { \"key\": value }"
        self.collapsed_fields = collapsed_fields
        self.json_dict = json_dict or {}

        super().__init__(*args, **kwargs)
        self.template = 'json_panel/resource_visualizer.html',

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update({
            'json_dict': self.json_dict,
            'collapsed_fields': self.collapsed_fields,
        })
        return kwargs

    class BoundPanel(Panel.BoundPanel):

        def render_html(self, parent_context: Mapping[str, Any] = None) -> str:
            context = {
                "collapsed_fields": self.panel.collapsed_fields,
                "html_fields": [],
                "resource": self.panel.json_dict,
            }
            return render_to_string(self.panel.template, context)
