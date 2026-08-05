from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import UserCreationForm, LoginForm
# Create your views here.


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    pass
