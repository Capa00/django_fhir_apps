# Template Panel
The template context can be static

    TemplatePanel(
        'my/path/to/template.html',
        get_context= {'var1': "Hello", 'var2': "World!!", ...},
        heading=_('Hello World Template')
    )

or calculated on instance

    TemplatePanel(
        'my/path/to/template.html',
        get_context= lambda instance: {'var1': instance.some_related_field.all(), ...},
        heading=_('Print all related')
    )

# Property Panel
With this panel you can print a property of your model in the modeladmin view

    PropertyPanel('my_property', heading=_('My property NAME')),
