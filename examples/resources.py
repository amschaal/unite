from applications import ApplicationResource
from resources.user_resource import UserResource

class FakeUserResource(ApplicationResource):
    application_id = 'fake_app'
    resource = UserResource
    def query_options(self,query):
        return [{'id':'one','name':'one','description':'Describe one'},{'id':'two','name':'two','description':'Describe two'}]
    def translate_response(self,response):
        #do something to response
        return response
    def get_by_id(self,id):
        return {'id':id,'name':'Example for id '+str(id),'foo':'bar'}