from unite import Singleton
from django.conf import settings
from collections import OrderedDict
from django.utils.module_loading import import_string
class ApplicationResource(object):
    application_id = None
    resource = None
    def query_options(self,query):
        raise NotImplementedError
    def translate_response(self,response):
        return response
    def get_by_id(self,id): #This should query remote API to get external representation
        raise NotImplementedError

