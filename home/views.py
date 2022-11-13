from enum import auto
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.models import Auto
from home.forms import AltaFormulario, BusquedaFormulario
from django.contrib import messages

def error_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
      
    return render(request, 'home/index.html')

def cargar_auto(request):
    formulario = AltaFormulario()
    
    if request.method == 'POST':
        formulario = AltaFormulario(data=request.POST)
        if formulario.is_valid():
            auto_nuevo = formulario.save()
            
            messages.success(request, 'El auto se ha guardado')
            auto_nuevo.marca
            auto_nuevo.modelo,


        
            return redirect('cargar')


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

