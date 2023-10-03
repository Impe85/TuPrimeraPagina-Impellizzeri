from django import forms

class ArcheryEquipmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    manufacturer = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.TextInput)

