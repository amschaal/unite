from rest_framework import serializers
from unite.models import ApplicationResource

class ApplicationResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationResource
        fields = '__all__'