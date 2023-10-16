from django.shortcuts import render, redirect
from .models import ArcheryEquipment
from .forms import ArcheryEquipmentForm, ArcheryEquipmentSearchForm

def add_equipment(request):
    if request.method == 'POST':
        form = ArcheryEquipmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            equipment = ArcheryEquipment(
                name=data.get('name'),
                manufacturer=data.get('manufacturer'),
                description=data.get('description')
            )
            equipment.save()
            return redirect('add_equipment') # Redirect back to form view 
        else:
            return render(request, 'inicio/inicio.html', {'form': form})
    
    else:
        form = ArcheryEquipmentForm() 
    
    return render(request, 'inicio/inicio.html', {'form': form})

def listado_equipment(request):
    formulario = ArcheryEquipmentSearchForm(request.GET)  # Asumiendo que tienes un formulario de búsqueda
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get('name')  # Usando 'name' como ejemplo, cambia según tu modelo
        equipos_encontrados = ArcheryEquipment.objects.filter(name__icontains=titulo_a_buscar)
    else:
        equipos_encontrados = ArcheryEquipment.objects.all()
    
    formulario = ArcheryEquipmentSearchForm()
    return render(request, 'inicio/listado_equipment.html', {'formulario': formulario, 'equipos_encontrados': equipos_encontrados})