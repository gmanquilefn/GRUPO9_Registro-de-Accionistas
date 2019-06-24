from django.db import models

# Create your models here.

class Accionista(models.Model):
    rut=models.CharField(max_length=12)
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    dirección=models.CharField(max_length=20)
    telefono=models.IntegerField()
    email=models.EmailField()
    fax=models.IntergerField()
    accionistas= models.Manager()
