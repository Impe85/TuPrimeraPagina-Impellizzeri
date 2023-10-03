from django.urls import path
from .views import add_equipment

urlpatterns = [
    path('', add_equipment, name='add_equipment'),
]
