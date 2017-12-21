from unite.applications import BaseApplicationResource, Application
from unite.resources.user_resource import UserResource

class FakeApplication(Application):
    id = 'fake_app'
    name = 'Fake App'
    description = 'Just an example app'

class FakeApplication2(Application):
    id = 'fake_app2'
    name = 'Fake App 2'
    description = 'Just an another example app'

data = [{'id':id,'name':'Name %d'%id,'description':'Describe %d'%id} for id in range(1,10)]

class FakeUserResource(BaseApplicationResource):
    application = FakeApplication
    resource = UserResource
    @staticmethod
    def query_resources(query):
        return data
    @staticmethod
    def get_by_id(id):
        return {'id':id,'name':'Name %s'%str(id),'description':'Describe %s'%str(id)}
    @staticmethod
    def get_id(obj):
        return obj.get('id')
    @staticmethod
    def get_label(obj):
        return obj.get('name')
    @staticmethod
    def get_description(obj):
        return obj.get('description')
    
class FakeUserResource2(FakeUserResource):
    application = FakeApplication2