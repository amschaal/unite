from resources import ResourcePlugin
class Application(object):
    id = 'example_app_id'
    app_resources = {}
    def register_resource(self,resource,app_resource):
        self.app_resources[]

class ApplicationResource(object):
    resource = ResourcePlugin
    def query_options(self,query):
        return [{'id':'one','name':'one','description':'Describe one'},{'id':'two','name':'two','description':'Describe two'}]
    def translate_response(self,response):
        return response
    def get_by_id(self,id): #This should query remote API to get external representation
        return {'id':id,'name':'Example for id '+str(id),'foo':'bar'}
    
class FakeApp(Application):
    id= 'fake_app'
    