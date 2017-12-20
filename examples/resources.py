from unite.applications import ApplicationResource, Application
from unite.resources.user_resource import UserResource

class FakeApplication(Application):
    id = 'fake_app'
    name = 'Fake App'
    description = 'Just an example app'

class FakeUserResource(ApplicationResource):
    application = FakeApplication
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