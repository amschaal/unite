from rest_framework import serializers
from unite.models import ApplicationResource, Resource

class ApplicationResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationResource
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    application_resources = ApplicationResourceSerializer(many=True, read_only=True)
    class Meta:
        model = Resource
        fields = '__all__'