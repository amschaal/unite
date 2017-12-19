from unite.resources import ResourcePlugin
from unite.resources.forms import ResourceForm
from django import forms

class UserResource(ResourcePlugin):
    id = 'user'
    name = 'User'
    description = ''

class UserResourceForm(ResourceForm):
    username = forms.CharField(max_length=30)
    first = forms.CharField(max_length=50,required=False)
    last = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=100,required=False)
    class Meta:
        fields = ('identifier','username','first','last','email')
