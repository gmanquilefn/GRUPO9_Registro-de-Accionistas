from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accionista.models import Accionista, Emisor
from traspaso.models import Acciones
from django.shortcuts import get_object_or_404
from django.db.models import Q


class AccionistasView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accionistas = Accionista.accionistas.all()
    if queryset:
      accionistas = Accionista.accionistas.filter(
        Q( nombres__icontains = queryset) |
        Q( apellidos__icontains = queryset) |
        Q( run__icontains = queryset)
      ).distinct()
    return render(request, 'accionistas.html', {'accionistas' : accionistas})

class CreateAccionista(LoginRequiredMixin, CreateView):
  model = Accionista
  template_name = './crear.html'
  fields = ['run', 'nombres', 'apellidos', 'nacionalidad', 'direccion', 'telefono', 'email', 'fax', 'firma']

class CreateEmisor(LoginRequiredMixin, CreateView):
  model = Emisor
  template_name = './emisor.html'
  fields = ['rut', 'nombreemisor', 'razonsocial']

class UpdateAccionista(LoginRequiredMixin, UpdateView):
  model = Accionista
  template_name = './editar.html'
  fields = ['nombres', 'apellidos', 'nacionalidad', 'direccion', 'telefono', 'email', 'fax', 'firma']

class DetalleAccionistaView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    accionista_id=kwargs["pk"]
    print(id)
    return render(request, 'accionista.html', {'accionista' : Accionista.accionistas.get(accionista_id=accionista_id)})

def FormularioVista(request):
  form = FormularioCrear(request.POST or None)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request,"formularionuevo.html",context)
