from django.db import models
from django.utils import timezone
from accionista.models import Accionista


class Acciones(models.Model):
  acciones_id = models.AutoField(primary_key=True)
  accionista_id = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  tercero_id = models.ManyToManyField('tercero.Tercero', blank=True, null=True)
  codigo = models.CharField(max_length=20, null=False, blank=False)
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

ESTADO_CHOICES = (
    ('espera','ESPERA'),
    ('aprobado', 'APROBADO'),
    ('rechazado','RECHAZADO'),
)

class Traspaso(models.Model):
  traspaso_id = models.AutoField(primary_key=True)
  acciones_id = models.ForeignKey(Acciones, on_delete=models.CASCADE, null=False, blank=False)
  run_venta = models.CharField(max_length=20, null=False, blank=False)
  run_compra = models.CharField(max_length=20, null=False, blank=False)
  estado = models.CharField(max_length=200, choices= ESTADO_CHOICES, default ='')
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  traspasos = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__(self):
    return self.estado