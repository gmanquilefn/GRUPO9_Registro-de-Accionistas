from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from traspaso.models import Acciones, Traspaso
from accionista.models import Accionista
from django.shortcuts import get_object_or_404
from django.db.models import Q

class AccionistasView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accioness = Acciones.acciones.all()
    if queryset:
      accioness = Acciones.acciones.filter(
        Q( accionista_id__run__icontains = queryset)
      ).distinct()
    return render(request, 'traspaso.html', {'accioness' : accioness})

class TraspasosView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    traspasos = Traspaso.traspasos.all()
    if queryset:
       traspasos = Traspaso.traspasos.filter(
        Q( run_venta__icontains = queryset) |
        Q( run_compra__icontains = queryset) |
        Q( acciones_id__codigo__icontains = queryset)
      ).distinct()
    return render(request, 'historial.html', {'traspasos' : traspasos})

class CreateTraspaso(LoginRequiredMixin, CreateView):
  model = Traspaso
  template_name = './creartraspaso.html'
  fields = ['acciones_id', 'run_venta','run_compra', 'estado']

class AccionesView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):

    return render(request, 'acciones.html')

class AccionesView2(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        acciones = Acciones.acciones.all()
        accionistas = Accionista.accionistas.all()
        context = {
            'acciones' : acciones,
            'accionistas' : accionistas
        }
        return render(request, 'editar3.html', context)

class CreateAcciones(LoginRequiredMixin, CreateView):
  model = Acciones
  template_name = './crear.html'
  fields = ['accionista_id', 'tercero_id','tipo', 'codigo', 'serie', 'cantidad', 'estado']

class UpdateAcciones(LoginRequiredMixin, UpdateView):
  model = Acciones
  template_name = './editar2.html'
  fields = ['tipo', 'serie', 'cantidad', 'estado']
