from typing import Mapping, Any

from django.template.loader import render_to_string
from wagtail.admin.panels import HelpPanel, Panel


class TemplatePanel(HelpPanel):

    def __init__(self, template_context=None, *args, **kwargs):
        self.template_context = template_context or {}
        super().__init__(*args, **kwargs)

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update({
            'template_context': self.template_context,
        })
        return kwargs

    class BoundPanel(Panel.BoundPanel):

        def render_html(self, parent_context: Mapping[str, Any] = None) -> str:
            context = self.panel.template_context(self.instance) if callable(self.panel.template_context) else self.panel.template_context
            return render_to_string(self.panel.template, context)
