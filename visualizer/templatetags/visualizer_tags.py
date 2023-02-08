from django import template

from visualizer.models import Resource

register = template.Library()


@register.filter
def split_camel_case(camel_case_string):
    return ''.join(map(lambda x: x if x.islower() else " "+x, camel_case_string))


@register.filter
def is_dict(obj):
    return isinstance(obj, dict)


@register.filter
def is_list(obj):
    return isinstance(obj, list)


@register.filter
def get_reference_id(resource_and_name):
    resource_type, name = resource_and_name.split("/")
    try:
        return Resource.objects.get(name=name).pk
    except Resource.DoesNotExist:
        return ''
