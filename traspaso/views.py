from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from traspaso.models import Acciones
from django.shortcuts import get_object_or_404
from django.db.models import Q

class AccionesView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    acciones = Acciones.acciones.all()
    return render(request, 'acciones.html', {'acciones' : acciones})

class CreateAcciones(LoginRequiredMixin, CreateView):
  model = Acciones
  template_name = './crear.html'
  fields = ['codigo', 'tipo', 'serie', 'cantidad', 'estado']