from wagtail.admin.panels import HelpPanel, Panel


class PropertyPanel(HelpPanel):
    def __init__(self, title=None, property=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.property = property
        self.title = title

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs['property'] = self.property
        kwargs['title'] = self.title
        return kwargs

    class BoundPanel(Panel.BoundPanel):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            assert self.panel.property is None or callable(self.panel.property), 'set function like "PropertyPanel(function=lambda instance: instance.something, title=..."'
            assert self.panel.title is None or callable(self.panel.title), 'set title like "PropertyPanel(title=lambda instance: f\"my title based on {instance}\"", function=...)'

            self.template_name = self.panel.template
            self.content = ''
            if self.panel.property:
                self.content = self.panel.property(self.instance)

            if self.panel.title:
                self.content = f"<h2>{self.panel.title(self.instance)}</h2><br>{self.content}"
