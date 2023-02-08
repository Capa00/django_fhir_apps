## PRE-SAVE
Pre save for CreateView and EditView

    class MyAdmin(EditableViewsModelAdmin):
        def create_pre_save(self, instance):
            ...
        
        def edit_pre_save(self, instance):
            ...


## POST-SAVE
Post save for CreateView and EditView

    class MyAdmin(EditableViewsModelAdmin):
        def create_post_save(self, instance):
            ...
        
        def edit_post_save(self, instance):
            ...

## CUSTOM QUERYSET
If you want to override the query of a field (example field name mY_fi3ld)

    class MyAdmin(EditableViewsModelAdmin):
        custom_quesryset = True
        
        def mY_fi3ld_field_queryset(self):
            return FieldModel.objects.filter(id__in=[1, 2, 3], ...)


## RUNTIME GENERATED VALUE
If you want a generated initial value of a field on runtime. In the example we see a random username generated for a user 

    class MyAdmin(EditableViewsModelAdmin):
        model = User
        create_generated_values = {'username': generate_random_username}
        
        def generate_random_username():
            return "".join([random.choices('abcdefgh') for _ in range(8)])

## PANELS CUSTOMIZATION
You can personalize create and edit panels and/or create and edit edit_handlers
    
    class MyAdmin(EditableViewsModelAdmin):
        model = User
        
        create_panels = [
            MultiFieldPanel([
                FieldPanel(
                    'username',
                    widget=forms.TextInput(attrs={'readonly': True})
                ),
                FieldPanel('email'),
            ], heading=_("User Info")),
        ]

        edit_panels = create_panels.copy()

        edit_handler_create = TabbedInterface([
            ObjectList(edit_panels, heading=_("Username and email")),
            ObjectList([
                FieldPanel('first_name'),
                FieldPanel('last_name'),
            ], heading=_("User full name")),
        ])

        edit_handler_edit = TabbedInterface([
            ObjectList(edit_panels, heading=_("Username and email")),
            ObjectList([
                FieldPanel('first_name'),
                FieldPanel('last_name'),
            ], heading=_("User full name")),
        ])

## OTHER OPTIONS
### create_redirect_to_edit and edit_redirect_to_edit
The save button in edit and create view redirect on edit view

    class MyAdmin(EditableViewsModelAdmin):
        create_redirect_to_edit = True
        edit_redirect_to_edit = True

### commit_on_create and commit_on_edit
If false the form save will not commit

    class MyAdmin(EditableViewsModelAdmin):
        commit_on_create = False
        commit_on_edit = False

### required_fields
This field will be required in form view

    class MyAdmin(EditableViewsModelAdmin):
        model = User
        required_fields = ['usename', 'email']