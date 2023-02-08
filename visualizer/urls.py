from django.urls import path
from .views import visualize_resource

urlpatterns = [
    path("<slug:resource_name>/<slug:resource_id>/", visualize_resource, name="visualize_resource"),
    path("list/<slug:resource_name>/", visualize_resource, name="visualize_resource"),
]
