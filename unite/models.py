from django.db import models
from django.contrib.auth.models import Group, User

class Uniter(models.Model):
    app_id = models.CharField(max_length=50)
    external_id = models.CharField(max_length=100)
    class Meta:
        abstract = True

class GroupUniter(Uniter):
    group = models.ForeignKey(Group)

class UserUniter(Uniter):
    user = models.ForeignKey(User)