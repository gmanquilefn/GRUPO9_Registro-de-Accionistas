from django.db import models

# Create your models here.

class Accionista(models.Model):
    run = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    totalAcciones = models.IntegerField()
    nacionalidad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    #fecha_Nacimiento = models.DateField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)
    fax = models.IntegerField()
    accionistas = models.Manager()