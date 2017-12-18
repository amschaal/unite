from resources import ResourcePlugin
from django import forms
from email import email

class UserResource(ResourcePlugin):
    id = 'user'
    name = 'User'
    description = ''

class UserResourceForm(forms.Form):
    username = forms.CharField(max_length=30)
    first = forms.CharField(max_length=50,required=False)
    last = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=100,required=False)
