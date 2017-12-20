from django.apps import AppConfig
from django.conf import settings
from unite.resources import ResourceTypes
from django.utils.module_loading import import_string

class UniteConfig(AppConfig):
    name = 'unite'
    verbose_name = "Unite"
    def ready(self):
        RT = ResourceTypes()
        for ar in getattr(settings,'APPLICATION_RESOURCES',[]):
            application_resource = import_string(ar)
            application_resource.resource._application_resources[application_resource.application.id] = application_resource
            print application_resource
#             @staticmethod
#     def get_application_resources(self):
#         app_resources = getattr(settings,'APPLICATION_RESOURCES')
#         for 