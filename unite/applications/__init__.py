class ApplicationResource(object):
    application_id = None
    resource = None
    def query_options(self,query):
        raise NotImplementedError
    def translate_response(self,response):
        return response
    def get_by_id(self,id): #This should query remote API to get external representation
        raise NotImplementedError

