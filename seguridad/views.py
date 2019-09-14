from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

class HomePageView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'index.html', context=None)
