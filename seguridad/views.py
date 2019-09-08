from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

class HomePageView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'index.html', context=None)

class BusquedaView(LoginRequiredMixin, UpdateView):
  def get(self, request, **kwargs):
    return render(request, 'busqueda.html', context=None)