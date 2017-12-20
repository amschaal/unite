from unite.applications import ApplicationResource
from unite.resources.user_resource import UserResource

class FakeUserResource(ApplicationResource):
    application_id = 'fake_app'
    resource = UserResource
    @staticmethod
    def query_options(query):
        return [{'id':'one','name':'one','description':'Describe one'},{'id':'two','name':'two','description':'Describe two'}]
    @staticmethod
    def translate_response(response):
        #do something to response
        return response
    @staticmethod
    def get_by_id(id):
        return {'id':id,'name':'Example for id '+str(id),'foo':'bar'}