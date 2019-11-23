from django.db import models
from django.utils import timezone
from tercero.models import Tercero
from traspaso.models import Acciones

class Accionista(models.Model):
  accionista_id = models.AutoField(primary_key=True)
  run = models.CharField(max_length=20, unique=True, null=False, blank=False)
  nombres = models.CharField(max_length=100, default='', null=False, blank=False)
  apellidos = models.CharField(max_length=100, default='', null=False, blank=False)
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
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  datos_accionistas = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__ (self):
    return self.accionista_id

class Firmas_Accionista(models.Model):
  accionista_id = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  firma1 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma2 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma3 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma4 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  firma5 = models.ImageField(upload_to="accionistas", blank=True, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  firmas_accionistas = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()
  
  def __str__(self):
    return self.accionista_id
