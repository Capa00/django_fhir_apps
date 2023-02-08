from wagtail.contrib.modeladmin.options import ModelAdmin

from .views import EditableCreateView, EditableEditView, EditableIndexView


class EditableViewsModelAdmin(ModelAdmin):
    custom_querysets = False
    required_fields = []

    index_view_class = EditableIndexView
    index_actions = []

    create_view_class = EditableCreateView
    create_panels = []
    create_generated_values = None
    create_post_save = None
    commit_on_create = True
    create_redirect_to_edit = False
    edit_handler_create = None

    edit_view_class = EditableEditView
    edit_panels = []
    edit_handler_edit = None
    commit_on_edit = True
    edit_redirect_to_edit = False
    edit_post_save = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.create_panels:
            self.create_panels = getattr(self, 'panels', [])
        if not self.edit_panels:
            self.edit_panels = getattr(self, 'panels', [])
