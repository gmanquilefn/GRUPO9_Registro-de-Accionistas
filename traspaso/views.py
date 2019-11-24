from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from traspaso.models import Acciones
from django.shortcuts import get_object_or_404
from django.db.models import Q


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
