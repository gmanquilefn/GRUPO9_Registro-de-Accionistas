from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from traspaso.models import Acciones
from accionista.models import Accionista
from django.shortcuts import get_object_or_404
from django.db.models import Q

class TraspasoView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
      queryset = request.GET.get("Buscar")
      acciones = Acciones.acciones.all()
      accionistas = Accionista.accionista.all()
      if queryset:
        acciones = Accionista.accionistas.filter(
          Q( run__icontains = queryset)
        ).distinct()
    return render(request, 'traspaso.html', {'acciones' : acciones}, {'accionista' : accionista})


class AccionesView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'acciones.html')

class CreateAcciones(LoginRequiredMixin, CreateView):
  model = Acciones
  template_name = './crear.html'
  fields = ['accionista_id', 'tercero_id','tipo', 'serie', 'cantidad', 'estado']

class UpdateAcciones(LoginRequiredMixin, UpdateView):
  model = Acciones
  template_name = './editar.html'
  fields = ['tipo', 'serie', 'cantidad', 'estado']
