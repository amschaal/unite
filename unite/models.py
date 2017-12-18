from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
import uuid

class ResourceType(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class Resource(models.Model):
    identifier = models.CharField(max_length=32,default=uuid.uuid4)
    type = models.ForeignKey(ResourceType)
    data = JSONField()
    class Meta:
        unique_together = (('type', 'identifier'),)

class Uniter(models.Model):
    resource = models.ForeignKey(Resource)
    app_id = models.CharField(max_length=50)
    external_id = models.CharField(max_length=100)
    data = JSONField(null=True)
    class Meta:
        abstract = True
        unique_together = (('resource', 'app_id'),)
