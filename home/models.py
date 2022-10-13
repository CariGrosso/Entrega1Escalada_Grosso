from django.db import models

class Auto(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=20)
    anio=models.IntegerField()
    km=models.IntegerField()
    color=models.CharField(max_length=30)
    precio=models.FloatField()
   