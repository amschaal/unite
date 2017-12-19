from django.shortcuts import render
from unite.resources import ResourceTypes

def resource_types(request):
    resource_types = ResourceTypes().get_all()
    return render(request, 'unite/resource_types.html', {'resource_types': resource_types})
def create_resource(request,type_id):
    resource_type = ResourceTypes().get(type_id)
    if request.method == 'GET':    
        form = resource_type.form()
    elif request.method == 'POST':
        form = resource_type.form(request.POST)
    return render(request, 'unite/resource_form.html', {'form': form})
    
    