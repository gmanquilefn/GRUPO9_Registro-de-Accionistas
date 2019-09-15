from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from tercero.models import Tercero
from django.shortcuts import get_object_or_404
from django.db.models import Q

class TercerosView(TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    terceros = Tercero.terceros.all()
    if queryset:
      terceros = Tercero.terceros.filter(
        Q( nombres__icontains = queryset) |
        Q( apellidos__icontains = queryset)
      ).distinct()
    return render(request, 'terceros.html', {'terceros' : terceros})

class CreateTercero(CreateView):
  model = Tercero
  template_name = './crear.html'
  fields = ['nombres', 'apellidos', 'rol', 'detalle', 'accionista_id']

class UpdateTercero(UpdateView):
  model = Tercero
  template_name = './editar.html'
  fields = ['rol', 'detalle']

class DetalleTerceroView(TemplateView):
  def get(self, request, **kwargs):
    id=kwargs["pk"]
    print(id)
    return render(request, 'tercero.html', {'tercero' : tercero.terceros.get(id=id)})

