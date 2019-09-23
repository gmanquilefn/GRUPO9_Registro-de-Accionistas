from django.db import models
from django.utils import timezone
from accionista.models import Accionista

class Tercero(models.Model):
  accionista_id = models.ForeignKey(Accionista, on_delete=models.CASCADE, null=False, blank=False)
  nombres = models.CharField(max_length=100, null=False)
  apellidos = models.CharField(max_length=100, null=False)
  rol = models.CharField(max_length=200)
  detalle = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)
  terceros = models.Manager()

  def update(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__(self):
    return self.accionista_id   