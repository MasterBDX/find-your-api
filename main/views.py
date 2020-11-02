from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from .models import ApiGuide

class HomeView(TemplateView):
    template_name = 'home.html'


class APIListView(ListView):
    context_object_name = 'apis'
    queryset = ApiGuide.objects.all()
    template_name = 'list.html'


class APIDetialView(DetailView):
    context_object_name = 'api'
    queryset = ApiGuide.objects.all()
    template_name = 'detail.html'