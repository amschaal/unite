from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
from unite import Singleton

class BaseResource(object):
    type_id = 'example_id' #override this
    name = 'Example resource type'
    description = 'Example description'
    form = None #This is the form that is used to create local Resources of this type
    _application_resources = OrderedDict()
    @classmethod
    def get_application_resources(cls):
        return cls._application_resources.values()
    @classmethod
    def get_application_resource(cls,app_id):
        return cls._application_resources.get(app_id,None)
    @staticmethod
    def get_label(instance):
        return instance.identifier

class ResourceTypes(object):
    __metaclass__ = Singleton
    def __init__(self):
        resources = getattr(settings,'RESOURCES')
        self._resources = OrderedDict()
        for r in resources:
            resource = import_string(r)
            self._resources[resource.type_id] = resource
    def get(self,type_id):
        return self._resources[type_id]
    def get_all(self):
        return self._resources.values()
