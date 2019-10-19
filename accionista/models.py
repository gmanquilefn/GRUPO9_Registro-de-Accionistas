from django.db import models
from django.utils import timezone
from tercero.models import Tercero

class Accionista(models.Model):
  run = models.CharField(max_length=20)
  nombres = models.CharField(max_length=100, default='')
  apellidos = models.CharField(max_length=100, default='')
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  acciones_id = models.ManyToManyField('accionista.Acciones', blank=False)
  accionistas = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__ (self):
    return self.nombres

  """def guardar(self, *args, **kwargs):
    if(self.end_date > self.start_date):"""

class Datos_Accionista(models.Model):
  run = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  nacionalidad = models.CharField(max_length=20, default='')
  direccion = models.CharField(max_length=60, default='')
  telefono = models.CharField(max_length=20, default='')
  email = models.CharField(max_length=100, default='example@correo.com')
  fax = models.CharField(max_length=20, null=True)
  Firma = models.FileField(upload_to="accionistas", blank=True, null=True)

  def __str__ (self):
    return self.run

class Firmas_Accionista(models.Model):
  run = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  firma1 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma2 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma3 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma4 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma5 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  
  def __str__(self):
    return self.run

class Datos_Acciones(models.Model):
  codigo = models.CharField(max_length=20, unique=True, blank=False)
  Tipo = models.CharField(max_length=20, default='', null=False)
  Serie = models.CharField(max_length=20, default='', null=False)
  Cantidad = models.IntegerField(default='',null = False)
  Estado = models.BooleanField(default=True)

  def __str__(self):
    return self.codigo

class Acciones(models.Model):
  Datos_Acciones_id = models.ForeignKey(Datos_Acciones,on_delete=models.CASCADE, null=False, blank=False)
  Accionista_id = models.ManyToManyField('accionista.Accionista', blank=False)
  Tercero_id = models.ManyToManyField('tercero.Tercero', blank=True)
  Rut_emisor = models.CharField(max_length=13,blank=False,null=False)