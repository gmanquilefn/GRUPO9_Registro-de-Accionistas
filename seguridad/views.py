from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from accionista.models import Accionista
from django.db.models import Q


class HomePageView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'index.html', context=None)

class BusquedaView(LoginRequiredMixin, UpdateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accioni = Accionista.accionistas.all()
    if queryset:
      accioni = Accionista.accionistas.filter(
        Q(nombres__icontains = queryset) |
        Q( apellidos__icontains = queryset) |
        Q( run__icontains = queryset)
      ).distinct()

    return render(request,'busqueda.html',{'accioni': accioni})
