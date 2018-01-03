from unite.resources import BaseResource
from unite.resources.forms import ResourceForm
from django import forms

class GroupResourceForm(ResourceForm):
    name = forms.CharField(max_length=50,required=True)

class GroupResource(BaseResource):
    type_id = 'group'
    name = 'Group'
    description = 'Manage groups across applications'
    form = GroupResourceForm
    @staticmethod
    def get_label(instance):
        return instance.data.get('name')

