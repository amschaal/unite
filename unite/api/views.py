from rest_framework.decorators import api_view
from rest_framework.response import Response
from unite.models import Resource, ApplicationResource
from unite.resources import ResourceTypes
from rest_framework.exceptions import APIException
from unite.api.serializers import ApplicationResourceSerializer

@api_view()
def get_app_resources(request,type_id,identifier,app_id):
    resource = Resource.objects.get(type_id=type_id,identifier=identifier)
    resource_type = ResourceTypes().get(type_id)
    print resource_type
    application_resource = resource_type.get_application_resource(app_id)
    if application_resource:
        query = request.query_params.get('query','')
        options = application_resource.query_options(query)
        return Response(options)
    else:
        raise APIException('No application resource with those parameters was found')
@api_view(['POST'])
def set_app_resource(request,type_id,identifier,app_id):
    resource = Resource.objects.get(type_id=type_id,identifier=identifier)
    resource_type = ResourceTypes().get(type_id)
    application_resource = resource_type.get_application_resource(app_id)
    if application_resource:
        id = request.data.get('id')
        obj = application_resource.get_by_id(id)
        id = application_resource.get_id(obj)
        instance, created = ApplicationResource.objects.get_or_create(resource=resource,app_id=application_resource.application.id)
        instance.data = obj
        instance.external_id = id
        instance.save()
        return Response({'resource':ApplicationResourceSerializer(instance).data,'translated':application_resource.translate_resource(obj)})
    else:
        raise APIException('No application resource with those parameters was found')