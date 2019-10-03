from django.db import models
from django.utils import timezone

class Accionista(models.Model):
  run = models.CharField(max_length=20)
  nombres = models.CharField(max_length=100, default='')
  apellidos = models.CharField(max_length=100, default='')
  totalAcciones = models.IntegerField(default=0)
  nacionalidad = models.CharField(max_length=20, default='')
  direccion = models.CharField(max_length=60, default='')
  telefono = models.CharField(max_length=20, default='')
  email = models.CharField(max_length=100, default='example@correo.com')
  fax = models.CharField(max_length=20, null=True)
  imagen = models.FileField(upload_to="accionistas", blank=True, null=True)
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
