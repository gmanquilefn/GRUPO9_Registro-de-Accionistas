from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from accionista import models
from accionista.models import Accionista


# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class HomePageView2(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'accionista_form.html', context=None)

class HomePageView3(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'creacion_acc.html', context=None)


class CreateAccionista(CreateView):
    model = Accionista
<<<<<<< HEAD
    template_name = './aaaa.html'
    fields = '__all__'

class UpdateAccionista(UpdateView):
    model = Accionista
    template_name = './aaaa.html'
    field = ['nombre', 'apellido', 'totalAcciones', 'nacionalidad', 'direccion', 'fecha_Nacimiento', 'telefono', 'email', 'fax']
=======
    template_name = './creacion_acc.html'
    fields = '_all_'
>>>>>>> 6f7627cb347e8399a3678b9819e59cec5f07105c
