from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
import uuid


"""
Resource contains instances of the above described ResourceTypes, such as a user or group.  Resources have a local unique identifier per type.
For example, for a "User" resources, the identifier may be "joebloggs".  There may only be 1 "joebloggs" for the "User" type.
The "data" field may contain additional local information for that resources.
"""
class Resource(models.Model):
    identifier = models.CharField(max_length=32,default=uuid.uuid4)
    type_id = models.CharField(max_length=30)
    data = JSONField()
    class Meta:
        unique_together = (('type_id', 'identifier'),)

"""
Uniter is the glue that unites resources across applications.  Each instance of a Uniter references a local Resource, which has a type.
That resources is then linked to resources in other applications using a combination of the app_id and external_id (the unique identifier of that resources in the other application).
The Uniter instance may also contain information about the external resources stored in the data field.  This may need to be updated periodically by querying the external applications API (or vice versa).
"""
class Uniter(models.Model):
    resource = models.ForeignKey(Resource)
    app_id = models.CharField(max_length=50)
    external_id = models.CharField(max_length=100)
    data = JSONField(null=True)
    class Meta:
        abstract = True
        unique_together = (('resources', 'app_id'),)
