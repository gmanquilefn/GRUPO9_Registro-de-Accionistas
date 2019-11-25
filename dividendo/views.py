from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dividendo.models import Pago_dividendo
from accionista.models import Accionista
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
class AccionistasView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accionistas = Accionista.accionistas.all()
    if queryset:
      accionistas = Accionista.accionistas.filter(
        Q( run__icontains = queryset)
      ).distinct()
    return render(request, 'pago.html', {'accionistas' : accionistas})

class AccionesView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):

    return render(request, 'dividendos.html')

class CreateAcciones(LoginRequiredMixin, CreateView):
  model = Pago_dividendo
  template_name = './crear.html'
  fields = ['accionista_id', 'monto','Estado_pago']

class UpdateAcciones(LoginRequiredMixin, UpdateView):
  model = Pago_dividendo
  template_name = './editar.html'
  fields = ['Estado_pago']