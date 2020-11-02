from django.views.generic import DetailView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView)
from django.views import View
from django.views.generic import (CreateView, DetailView)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.urls import reverse_lazy
from django.http import Http404

from .forms import (LoginForm, RegistrationForm,)
from .models import UserProfile

User = get_user_model()


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', None)
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)
        raise Http404


class UserLogoutView(LogoutView):
    next_page = 'accounts:login'


class UserProfileView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/profile.html'
    slug_url_kwarg = 'user_slug'


class UserRegistrerView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = '/'
