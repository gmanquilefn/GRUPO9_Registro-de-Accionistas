from django.db import models
from django.utils import timezone
from tercero.models import Tercero

class Accionista(models.Model):
  accionista_id = models.AutoField(primary_key=True)
  run = models.CharField(max_length=20, unique=True, null=False, blank=False)
  nombres = models.CharField(max_length=100, default='', null=False, blank=False)
  apellidos = models.CharField(max_length=100, default='', null=False, blank=False)
  acciones_id = models.ManyToManyField('accionista.Acciones', blank=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  accionistas = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__ (self):
    return self.nombres

  """def guardar(self, *args, **kwargs):
    if(self.end_date > self.start_date):"""

class Datos_Accionista(models.Model):
  accionista_id = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  nacionalidad = models.CharField(max_length=20, default='')
  direccion = models.CharField(max_length=60, default='')
  telefono = models.CharField(max_length=20, default='')
  email = models.CharField(max_length=100, default='example@correo.com')
  fax = models.CharField(max_length=20, null=True)
  Firma = models.FileField(upload_to="accionistas", blank=True, null=True)

  def __str__ (self):
    return self.nacionalidad

class Firmas_Accionista(models.Model):
  accionista_id = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  firma1 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma2 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma3 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma4 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma5 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  
  def __str__(self):
    return self.firma1


class Acciones(models.Model):
  acciones_id = models.AutoField (primary_key=True)
  tercero_id = models.ManyToManyField('tercero.Tercero', blank=True)
  rut_emisor = models.CharField(max_length=13,blank=False,null=False)
  
  def __str__(self):
    return self.acciones_id

class Datos_Acciones(models.Model):
  acciones_id = models.ForeignKey(Acciones, on_delete=models.CASCADE, null=False, blank=False)
  codigo = models.CharField(max_length=20, unique=True, blank=False)
  Tipo = models.CharField(max_length=20, default='', null=False)
  Serie = models.CharField(max_length=20, default='', null=False)
  Cantidad = models.IntegerField(default='',null = False)
  Estado = models.BooleanField(default=True)

  def __str__(self):
    return self.codigo