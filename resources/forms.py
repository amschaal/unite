from django import forms
from unite.models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('identifier',)