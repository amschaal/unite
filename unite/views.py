from django.shortcuts import render, redirect
from unite.resources import ResourceTypes
from unite.models import Resource

def resource_types(request):
    resource_types = ResourceTypes().get_all()
    return render(request, 'unite/resource_types.html', {'resource_types': resource_types})
def create_resource(request,type_id):
    resource_type = ResourceTypes().get(type_id)
    if request.method == 'GET':    
        form = resource_type.form()
    elif request.method == 'POST':
        form = resource_type.form(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            resource = Resource.objects.create(identifier=cleaned['identifier'],type_id=type_id,data=cleaned)
            return redirect('resource', type_id=type_id,identifier=resource.identifier)
    return render(request, 'unite/resource_form.html', {'form': form})
    
def resource(request,type_id,identifier):
    resource_type = ResourceTypes().get(type_id)
    resource = Resource.objects.get(type_id=type_id,identifier=identifier)
    return render(request, 'unite/resource.html', {'resource': resource,'resource_type':resource_type})    