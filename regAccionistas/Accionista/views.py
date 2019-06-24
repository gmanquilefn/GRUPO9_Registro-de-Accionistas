from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class AccionistaCreate(CreateView):
    model = Accionista
    template_name='./accionista_form.html'
    fields= '_all_'

class AccionistaUpdate(UpdateView):
    model = Accionista
    template_name = './accionista_form.html'
    fields = ['rut', 'nombres', 'apellidos', 'dirección', 'telefono', 'email', 'fax']
