from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accionista import models
from accionista.views import CreateAccionista


# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class HomePageView2(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'accionista_form.html', context=None)

