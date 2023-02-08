from django import forms
from django.utils.translation import gettext as _
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.modeladmin.options import modeladmin_register

from editable_admin.admin import EditableViewsModelAdmin
from wagtail_panels.panels import PropertyPanel
from visualizer.panels import FhirResourceVisualizerPanel
from .models import Resource, ResourceType


@modeladmin_register
class ResourceAdmin(EditableViewsModelAdmin):
    model = Resource
    menu_label = 'FHIR Resources'
    list_filter = ('resource_type',)
    list_display = ('name', 'resource_type')  # , 'mpId')
    search_fields = list_display
    menu_icon = "form"

    edit_panels = [
        PropertyPanel(
            title=lambda instance: f"{instance.resource_type}<br><br>&emsp;>&ensp;{instance.name}"),

        # JsonVisualizerPanel(
        #     heading=_("JSON Panel"),
        #     json_dict={
        #         "1.1" : {
        #             "2.1" : "----------"
        #         },
        #         "1.2": ["2.2", "2.3"]
        #     },
        #     collapsed_fields=["1.1"]
        # ),

        FhirResourceVisualizerPanel(
            heading=_("FHIR Panel"),
            resource_type=lambda instance: instance.resource_type,
            resource_id=lambda instance: instance.name,
            collapsed_fields=["meta", "text"]
        ),

        FieldPanel('data', widget=forms.Textarea, heading=_("Data"))
    ]

    create_panels = [
        FieldPanel("resource_type"),
        FieldPanel("name"),
        FieldPanel('data', widget=forms.Textarea)
    ]


@modeladmin_register
class ResourceTypeAdmin(EditableViewsModelAdmin):
    model = ResourceType
    menu_label = 'FHIR Resource Types'
    list_display = ('name',)
    search_fields = list_display

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .wagtail_hooks import UpdateResourcesBulkAction
        self.index_actions = [UpdateResourcesBulkAction]

    panels = [FieldPanel('name')]

