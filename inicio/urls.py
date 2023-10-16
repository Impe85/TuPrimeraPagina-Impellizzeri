from django.urls import path
from .views import add_equipment
from .views import listado_equipment

urlpatterns = [
    path('', add_equipment, name='add_equipment'),
    path('listado/', listado_equipment, name='listado_equipment'),
]
