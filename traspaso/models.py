from django.db import models
from django.utils import timezone



class Acciones(models.Model):
  acciones_id = models.AutoField (primary_key=True)
  accionista_id = models.ManyToManyField('accionista.Accionista', blank=False)
  tercero_id = models.ManyToManyField('tercero.Tercero', blank=True, null=True)
  codigo = models.CharField(max_length=20, unique=True, null=False, blank=False)
  tipo = models.CharField(max_length=20, default='', null=False)
  serie = models.CharField(max_length=20, default='', null=False)
  cantidad = models.IntegerField(default='',null = False)
  estado = models.CharField(max_length=20, default='', null=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  acciones = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__(self):
    return self.codigo
