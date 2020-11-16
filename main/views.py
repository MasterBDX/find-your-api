from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import BaseCreateView
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView)

from .models import ApiGuide,SiteInfo,Suggestion
from .forms import AddSuggestionForm


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
    context_object_name = 'guide'
    queryset = ApiGuide.objects.all()
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddSuggestionForm()
        return context

class AddSuggestionView(SuccessMessageMixin,BaseCreateView):
    form_class = AddSuggestionForm
    queryset = Suggestion.objects.all()
    success_message = 'Thanks for your suggestion &nbsp; <i class="fas fa-thumbs-up fa-lg"></i>'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        self.success_url = reverse_lazy('main:detail',kwargs={'slug':self.kwargs.get('slug')})
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url) + '#suggestion'  # success_url may be lazy  
        