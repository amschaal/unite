from unite import Singleton
from django.conf import settings
from collections import OrderedDict
from django.utils.module_loading import import_string
class ApplicationResource(object):
    application_id = None
    resource = None
    @staticmethod
    def query_options(query):
        raise NotImplementedError
    @staticmethod
    def translate_response(response):
        return response
    @staticmethod
    def get_by_id(id): #This should query remote API to get external representation
        raise NotImplementedError

