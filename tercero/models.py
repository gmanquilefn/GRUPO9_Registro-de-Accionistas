from django.db import models
from django.utils import timezone

ROL_CHOICES = (
  ('apoderado','APODERADO'),
  ('corredor', 'CORREDOR'),
  ('representante','REPRESENTANTE'),
)

class Tercero(models.Model):
  tercero_id = models.AutoField(primary_key=True)
  accionista_id = models.ManyToManyField('accionista.Accionista', blank=False)
  run = models.CharField(max_length=20, null=False, blank=False)
  nombres = models.CharField(max_length=100, null=False)
  apellidos = models.CharField(max_length=100, null=False)
  rol = models.CharField(max_length=200, choices= ROL_CHOICES, default ='')
  poder = models.BooleanField()
  firma = models.ImageField(upload_to="terceros", blank=True, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  terceros = models.Manager()

  def update(self):
    self.firma = models.ImageField(upload_to="terceros", blank=True, null=True)
    self.updated_at = timezone.now()
    self.save()

  def __str__(self):
    return self.nombres
