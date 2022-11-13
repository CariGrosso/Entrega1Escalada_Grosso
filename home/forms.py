from django import forms
from django.forms import ModelForm
from home.models import Auto
class AltaFormulario(ModelForm):
    class Meta:
        model = Auto
        fields = ['marca',
    'modelo',
    'anio',
    'km',
    'color',
    'precio',]
    

class BusquedaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    