from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workspace
from .forms import WorkspaceForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class WorkspaceListView(LoginRequiredMixin, ListView):
    model = Workspace
    template_name = "workspaces/workspace_list.html"
    context_object_name = "workspaces"

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        busqueda = self.request.GET.get("busqueda", "")
        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset


class WorkspaceCreateView(LoginRequiredMixin, CreateView):
    template_name = "workspaces/crear_workspace.html"
    form_class = WorkspaceForm
    success_url = reverse_lazy("listar_workspaces")


class WorkspaceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "workspaces/editar_workspace.html"
    form_class = WorkspaceForm
    success_url = reverse_lazy("listar_workspaces")


class WorkspaceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "workspaces/eliminar_workspace.html"
    form_class = WorkspaceForm
    success_url = reverse_lazy("listar_workspaces")
