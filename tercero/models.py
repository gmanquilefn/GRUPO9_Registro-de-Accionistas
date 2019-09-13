from django.db import models
from django.utils import timezone

class Tercero(models.Model):
  accionista_id = models.ForeignKey('accionista.id', on_delete=models.CASCADE)
  nombres = models.CharField(max_length=100, default='')
  apellidos = models.CharField(max_length=100, default='')
  rol = models.CharField(max_length=200)
  text = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.updated_at = timezone.now()
    self.save()

  def __str__(self):
    return self.accionista_id   