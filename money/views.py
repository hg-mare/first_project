from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

from . import forms

class TopView(TemplateView):
    template_name="money/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name="money/home.html"

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name="money/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name="money/login.html"