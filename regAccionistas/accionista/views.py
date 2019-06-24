from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accionista.models import Accionista
# Create your views here.


class CreateAccionista(CreateView):
    model = Accionista
    template_name = './accionista_form.html'
    fields = '_all_'


class HomePageView2(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'accionista_form.html', context=None)