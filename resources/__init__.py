class ResourcePlugin(object):
    id = 'example_id' #override this
    name = 'Example resource type'
    description = 'Example description'
    form = None #This is the form that is used to create local Resources of this type
    def add_app(self,app):
        pass

