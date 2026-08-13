from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from projects.models import Project

# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/listar_tareas.html"
    context_object_name = "tareas"

    def get_queryset(self):
        queryset = super().get_queryset()
        project = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        busqueda = self.request.GET.get("busqueda", "").strip()
        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset.filter(project=project)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyecto"] = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/crear_tarea.html"
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        form.instance.project = project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyecto"] = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        return context

    def get_success_url(self):
        return reverse_lazy(
            "listar_tareas", kwargs={"proyecto_id": self.kwargs["proyecto_id"]}
        )


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/editar_tarea.html"
    form_class = TaskForm
    context_object_name = "tarea"

    def get_queryset(self):
        queryset = super().get_queryset()
        project = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        return queryset.filter(project=project)

    def success_url(self):
        return reverse_lazy(
            "listar_tareas", kwargs={"proyecto_id": self.kwargs["proyecto_id"]}
        )


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/eliminar_tarea.html"
    context_object_name = "tarea"

    def get_queryset(self):
        queryset = super().get_queryset()
        project = get_object_or_404(
            Project, id=self.kwargs["proyecto_id"], workspace__owner=self.request.user
        )
        return queryset.filter(project=project)

    def get_success_url(self):
        return reverse_lazy(
            "listar_tareas", kwargs={"proyecto_id": self.kwargs["proyecto_id"]}
        )
