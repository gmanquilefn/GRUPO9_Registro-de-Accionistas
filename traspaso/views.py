from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from traspaso.models import Acciones
from accionista.models import Accionista
from django.shortcuts import get_object_or_404
from django.db.models import Q

class AccionistasView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accionistas = Accionista.accionistas.all()
    if queryset:
      accionistas = Accionista.accionistas.filter(
        Q( run__icontains = queryset)
      ).distinct()
    return render(request, 'traspaso.html', {'accionistas' : accionistas})


class AccionesView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'acciones.html')

class CreateAcciones(LoginRequiredMixin, CreateView):
  model = Acciones
  template_name = './crear.html'
  fields = ['accionista_id', 'tercero_id', 'emisor_id', 'tipo', 'serie', 'cantidad', 'estado']

class UpdateAcciones(LoginRequiredMixin, UpdateView):
  model = Acciones
  template_name = './editar.html'
  fields = ['tipo', 'serie', 'cantidad', 'estado']
