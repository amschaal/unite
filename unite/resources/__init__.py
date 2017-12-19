from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class BaseResource(object):
    type_id = 'example_id' #override this
    name = 'Example resource type'
    description = 'Example description'
    form = None #This is the form that is used to create local Resources of this type
#     def get_form(self):

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
