from django.shortcuts import render, redirect
from .models import ArcheryEquipment
from .forms import ArcheryEquipmentForm

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