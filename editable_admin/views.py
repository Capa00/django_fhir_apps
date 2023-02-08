from abc import ABC

from django.urls import reverse
from django.utils.safestring import mark_safe
from wagtail.admin.edit_handlers import ObjectList
from wagtail.contrib.modeladmin.views import ModelFormView, CreateView, EditView, IndexView


class EditableView(ABC, ModelFormView):
    def yield_internal_panels(self, panels):
        if not panels: raise StopIteration
        # entra dentro i multifieldpanels ricorsivamente e ritorna solo i panel interni
        for panel in panels:
            if hasattr(panel, 'children'):
                yield from self.yield_internal_panels(panel.children)
            else:
                yield panel

    def get_form(self):
        def deco(form_save):
            def wr(*args, **kwargs):
                instance = self.get_instance()
                phase = 'edit' if instance.pk else 'create'

                if hasattr(self.model_admin, f'{phase}_pre_save') and callable(getattr(self.model_admin, f'{phase}_pre_save')):
                    getattr(self.model_admin, f'{phase}_pre_save')(instance)

                commit = getattr(self.model_admin, f'commit_on_{phase}', True)
                instance = form_save(commit=commit, *args, **kwargs)
                if hasattr(self.model_admin, f'{phase}_post_save') and callable(getattr(self.model_admin, f'{phase}_post_save')):
                    getattr(self.model_admin, f'{phase}_post_save')(instance)

                return instance

            return wr

        form = super().get_form()
        if self.model_admin.custom_querysets:
            for field_name, field in form.fields.items():
                if field_name in self.model_admin.required_fields:
                    setattr(field, 'required', True)
                custom_query = getattr(self.model_admin, f'{field_name}_field_queryset', None)
                if custom_query is None:
                    continue
                if callable(custom_query):
                    field.queryset = custom_query()
                else:
                    raise AttributeError(f'{field_name}_field_queryset must be a callable')

        form.save = deco(form.save)
        return form


class EditableCreateView(CreateView, EditableView):
    def _assign_generated_value(self, generated_values):
        if generated_values:
            for panel in self.yield_internal_panels(self.model_admin.create_panels):
                field_name = getattr(panel, 'field_name', None) or getattr(panel, 'relation_name')
                generator = generated_values.get(field_name)
                if generator:
                    panel.widget.attrs['value'] = generated_values[field_name]()  # Testato solo coi campi di testo

    def get_edit_handler(self):
        generated_values = getattr(self.model_admin, 'create_generated_values', None)
        self._assign_generated_value(generated_values)  # Testato solo coi campi di testo

        edit_handler = ObjectList(self.model_admin.create_panels)
        return edit_handler.bind_to_model(self.model_admin.model)
        # return edit_handler.bind_to(model=self.model_admin.model, request=self.request, instance=self.get_instance())

    def get_success_url(self):
        url = self.index_url
        if self.model_admin.create_redirect_to_edit:
            url += f"edit/{self.instance.id}"
        return url


class EditableEditView(EditView, EditableView):
    def get_edit_handler(self):
        if self.model_admin.edit_handler_edit:
            edit_handler = self.model_admin.edit_handler_edit
        else:
            edit_handler = ObjectList(self.model_admin.edit_panels)
        return edit_handler.bind_to_model(self.model_admin.model)
        # return edit_handler.bind_to(model=self.model_admin.model, request=self.request, instance=self.get_instance())

    def get_success_url(self):
        url = self.index_url
        if self.model_admin.edit_redirect_to_edit:
            url += f"edit/{self.instance.id}"
        return url


class EditableIndexView(IndexView):
    def get_buttons_for_obj(self, obj):
        super_btns = super().get_buttons_for_obj(obj)
        btns = getattr(self.model_admin, 'index_actions', [])
        btns = [{
            'url': reverse('wagtail_bulk_action', args=[obj._meta.app_label, obj._meta.model_name, x.action_type]) + f"?id={obj.id}",
            'label': x.display_name,
            'classname': 'button button-secondary button-small',
            'title': x.aria_label
        } for x in btns]
        return super_btns + btns
