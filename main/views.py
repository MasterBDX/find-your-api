from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from .models import ApiGuide,SiteInfo


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = SiteInfo.objects.last() 
        return context
    
        


class APIListView(ListView):
    context_object_name = 'apis'
    queryset = ApiGuide.objects.all()
    template_name = 'list.html'


class APIDetialView(DetailView):
    context_object_name = 'api'
    queryset = ApiGuide.objects.all()
    template_name = 'detail.html'