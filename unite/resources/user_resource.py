from unite.resources import BaseResource
from unite.resources.forms import ResourceForm
from django import forms

class UserResourceForm(ResourceForm):
    username = forms.CharField(max_length=30)
    first = forms.CharField(max_length=50,required=False)
    last = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=100,required=False)
#     class Meta:
#         fields = ('identifier','username','first','last','email')

class UserResource(BaseResource):
    type_id = 'user'
    name = 'User'
    description = 'Manage users across applications'
    form = UserResourceForm
    @staticmethod
    def get_label(instance):
        return '(%s) %s, %s'%(instance.data.get('username',''),instance.data.get('last',''),instance.data.get('first'))

