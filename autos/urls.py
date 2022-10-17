from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('cargar_auto/', views.cargar_auto, name='cargar'),
    path('ver_auto/', views.ver_autos, name='ver'),   
    path('admin/', admin.site.urls),  
]
