from django.db import models

class Accionista(models.Model):
    run = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=100, default='')
    totalAcciones = models.IntegerField(default=0)
    nacionalidad = models.CharField(max_length=20, default='')
    direccion = models.CharField(max_length=40, default='')
    #fecha_Nacimiento = models.DateField()
    telefono = models.IntegerField(default=0)
    email = models.CharField(max_length=100, default='example@correo.com')
    fax = models.IntegerField(default=0)
    accionistas = models.Manager()
