from abc import ABC

from wagtail.admin.views.bulk_action import BulkAction


class ListedBulkAction(BulkAction, ABC):
    def get_actionable_objects(self):
        objects = []
        items_with_no_access = []
        object_ids = self.request.GET.get("id", "-1").split(',')
        if "all" in object_ids:
            object_ids = self.get_all_objects_in_listing_query(
                self.request.GET.get("childOf")
            )

        for obj in self.get_queryset(self.model, object_ids):
            if not self.check_perm(obj):
                items_with_no_access.append(obj)
            else:
                objects.append(obj)
        return objects, {"items_with_no_access": items_with_no_access}