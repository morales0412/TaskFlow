from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
# Create your views here.


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        print("Entro al form_valid")
        user = form.save()
        login(self.request, user)
        return redirect("listar_workspaces")


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    pass
