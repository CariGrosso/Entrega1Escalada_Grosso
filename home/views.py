from enum import auto
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.models import Auto
from home.forms import AltaFormulario, BusquedaFormulario



def index(request):
      
    return render(request, 'home/index.html')

def cargar_auto(request):
    
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST['modelo']
        anio = request.POST['anio']
        km = request.POST['km']
        color = request.POST['color']
        precio = request.POST['precio']
        auto = Auto(marca=marca, modelo=modelo, anio=anio, km=km, color=color, precio=precio)
        auto.save()

        return redirect('cargar')
        formulario = AltaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            marca = data['marca']
            modelo = data['modelo']
            anio = data['anio']
            km = data['km']
            color = data['color']
            precio = data['precio']
            auto = Auto(marca=marca, modelo=modelo, anio=anio, km=km, color=color, precio=precio)
            auto.save()

            return redirect('cargar')
    return render(request, 'home/cargar_auto.html', {})
    formulario = AltaFormulario()

    return render(request, 'home/cargar_auto.html', {'formulario': formulario})


def ver_autos(request):

    vehiculos = Auto.objects.all()
    marca = request.GET.get('marca', None)

    if marca:
        vehiculos = Auto.objects.filter(marca__icontains=marca)
    else:
        vehiculos = Auto.objects.all()

    
    formulario = BusquedaFormulario()

    return render(request, 'home/ver_auto.html', {'vehiculos': vehiculos})
    return render(request, 'home/ver_auto.html', {'vehiculos': vehiculos, 'formulario': formulario}) 

