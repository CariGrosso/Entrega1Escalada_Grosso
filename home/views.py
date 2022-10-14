from enum import auto
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.models import Auto




def nosotros(request):
      
    return render(request, 'padre/index.html')
