from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
import uuid

"""
ResourceType may be any type of relation you want to maintain across applications.  IE: Group, User, Account, etc.
"""
class ResourceType(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

"""
Resource contains instances of the above described ResourceTypes, such as a user or group.  Resources have a local unique identifier per type.
For example, for a "User" resource, the identifier may be "joebloggs".  There may only be 1 "joebloggs" for the "User" ResourceType.
The "data" field may contain additional local information for that resource.
"""
class Resource(models.Model):
    identifier = models.CharField(max_length=32,default=uuid.uuid4)
    type = models.ForeignKey(ResourceType)
    data = JSONField()
    class Meta:
        unique_together = (('type', 'identifier'),)

"""
Uniter is the glue that unites resources across applications.  Each instance of a Uniter references a local Resource, which has a type.
That resource is then linked to resources in other applications using a combination of the app_id and external_id (the unique identifier of that resource in the other application).
The Uniter instance may also contain information about the external resource stored in the data field.  This may need to be updated periodically by querying the external applications API (or vice versa).
"""
class Uniter(models.Model):
    resource = models.ForeignKey(Resource)
    app_id = models.CharField(max_length=50)
    external_id = models.CharField(max_length=100)
    data = JSONField(null=True)
    class Meta:
        abstract = True
        unique_together = (('resource', 'app_id'),)
