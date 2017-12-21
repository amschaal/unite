from unite import Singleton
from django.conf import settings
from collections import OrderedDict
from django.utils.module_loading import import_string

class Application(object):
    id = None
    name = None
    description = None

class BaseApplicationResource(object):
    application = None
    resource = None
    @staticmethod
    def query_resources(query): #This should query remote API to get external representation
        raise NotImplementedError
    @classmethod
    def query_options(cls,query):
        return cls.translate_response(cls.query_resources(query))
    @classmethod
    def translate_resource(cls,obj):
        return {'id':cls.get_id(obj),'label':cls.get_label(obj),'description':cls.get_description(obj)}
    @classmethod
    def translate_response(cls,response):
        return [cls.translate_resource(obj) for obj in response]
    @staticmethod
    def get_by_id(id): 
        raise NotImplementedError
    @staticmethod
    def get_id(obj):
        raise NotImplementedError
    @staticmethod
    def get_label(obj):
        raise NotImplementedError
    @staticmethod
    def get_description(obj):
        return ''

