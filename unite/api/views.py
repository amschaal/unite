from rest_framework.decorators import api_view
from rest_framework.response import Response
from unite.models import Resource
from unite.resources import ResourceTypes
from rest_framework.exceptions import APIException

@api_view()
def get_app_resources(request,type_id,identifier,app_id):
    resource = Resource.objects.get(type_id=type_id,identifier=identifier)
    resource_type = ResourceTypes().get(type_id)
    application_resource = resource_type.get_application_resource(app_id)
    print 'application_resource'
    print application_resource
    if application_resource:
        query = request.query_params.get('query','')
        options = application_resource.query_options(query)
        return Response(options)
    else:
        raise APIException('No application resource with those parameters was found')