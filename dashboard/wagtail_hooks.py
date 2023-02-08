from wagtail import hooks

from visualizer.admin import ResourceAdmin, ResourceTypeAdmin


@hooks.register('construct_main_menu')
def hide_explorer_menu_item_from_frank(request, menu_items):
    if request.user.username != 'superuser':
        show_item = [ResourceAdmin.menu_label, ResourceTypeAdmin.menu_label]
        menu_items[:] = [item for item in menu_items if item.label in show_item]
