from django import forms

class AltaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=20)
    anio=forms.IntegerField()
    km=forms.IntegerField()
    color=forms.CharField(max_length=30)
    precio=forms.FloatField()


class BusquedaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)