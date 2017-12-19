from django import forms
from unite.models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
        exclude = ('type_id','data')