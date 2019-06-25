from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from accionista import models
from accionista.models import Accionista

class HomePageView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AccionistasView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'accionistas.html', {'accionistas' : Accionista.accionistas.all()})

class CreateAccionista(LoginRequiredMixin, CreateView):
    model = Accionista
    template_name = './crear.html'
    fields = '__all__'

class UpdateAccionista(LoginRequiredMixin, UpdateView):
    model = Accionista
    template_name = './editar.html'
    fields = ['nombre', 'apellido', 'totalAcciones', 'nacionalidad', 'direccion', 'telefono', 'email', 'fax']

class DetalleAccionistaView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'accionista.html', {'accionista' : Accionista.accionistas.get(id=id)})