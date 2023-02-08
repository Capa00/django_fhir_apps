from django.template.response import TemplateResponse

from visualizer.fake_resources import Resources


def visualize_resource(request, resource_name, resource_id):
    context = {"resource": Resources.MedicationProductDefinition}
    return TemplateResponse(request, 'visualizer/resource_visualizer.html', context)


def visualize_resources_list(request, resource_name):
    context = {"resource": Resources.AdministrableProductDefinitionBundle}
    return TemplateResponse(request, 'visualizer/resources_list_visualizer.html')

