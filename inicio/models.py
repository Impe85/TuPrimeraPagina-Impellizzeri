from django.db import models

class ArcheryEquipment(models.Model):
    name = models.CharField(max_length=255) # Name for the equipment.
    manufacturer = models.CharField(max_length=255) # Fabricator.
    description = models.TextField() #Description for the equipment.
