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
    template_name = './creacion_acc.html'
    fields = '_all_'

