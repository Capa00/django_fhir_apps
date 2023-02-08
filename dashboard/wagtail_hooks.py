from django.utils.safestring import mark_safe
from wagtail import hooks
from wagtail.admin.ui.components import Component

from visualizer.admin import ResourceAdmin, ResourceTypeAdmin


@hooks.register('construct_main_menu')
def hide_explorer_menu_item_from_frank(request, menu_items):
    if request.user.username != 'superuser':
        show_item = [ResourceAdmin.menu_label, ResourceTypeAdmin.menu_label]
        menu_items[:] = [item for item in menu_items if item.label in show_item]


class WelcomePanel(Component):
    order = 50
    name = "home_dashboard"
    template_name = "home_dashboard.html"


@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.clear()
    panels.append(WelcomePanel())
