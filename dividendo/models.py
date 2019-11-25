from django.db import models
from django.utils import timezone
from accionista.models import Accionista
# Create your models here.

class Pago_dividendo(models.Model):
    pago_id = models.AutoField ( primary_key=True)
    accionista_id = models.ForeignKey(Accionista, blank=False, null=False, on_delete=models.CASCADE)
    monto = models.IntegerField(blank=False, null=False)
    ESTADO_CHOICES = (
        ('REALIZADO', 'Realizado'),
        ('PENDIENTE', 'Pendiente'),
    )
    Estado_pago = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    Pago_dividendos = models.Manager()

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__ (self):
        return self.pago_id