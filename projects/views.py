from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from workspaces.models import Workspace
# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/listar_proyectos.html"
    context_object_name = "proyectos"

    def get_queryset(self):
        # self.kwargs["nombre_variable"] contiene los parametros que se le pasa por la URL
        queryset = super().get_queryset()
        # se obtiene el objeto del workspace al que pertenece el proyecto
        workspace = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        # Como workspace es un objeto relacionado mediante una ForeignKey, Django puede utilizar su PK para realizar la consulta.
        queryset = queryset.filter(workspace=workspace)
        busqueda = self.request.GET.get("busqueda", "").strip()

        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        # Se obtiene el contexto que Django ya preparó para la vista
        context = super().get_context_data(**kwargs)
        # se obtiene el objeto del workspace al que pertenece el proyecto y se añade al contexto para poder mostrarlo en la plantilla
        context["workspace"] = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        # contexto nuevo que se le pasa a la plantilla , la queryset y el objeto añadido
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/crear_proyecto.html"
    form_class = ProjectForm

    def form_valid(self, form):
        workspace = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        form.instance.workspace = workspace

        if Project.objects.filter(
            workspace=workspace, name=form.instance.name
        ).exists():
            form.add_error(
                "name", "Ya existe un proyecto con este nombre en este workspace."
            )
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        # Se usa aca el success ya que se puede acceder a los kwargs de la URL y se puede redirigir a la lista de proyectos del workspace correspondiente
        return reverse_lazy(
            "listar_proyectos", kwargs={"workspace_id": self.kwargs["workspace_id"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workspace"] = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        return context


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "projects/editar_proyecto.html"
    form_class = ProjectForm
    context_object_name = "proyecto"

    def get_queryset(self):
        queryset = super().get_queryset()
        workspace = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        return queryset.filter(workspace=workspace)

    def get_success_url(self):
        return reverse_lazy(
            "listar_proyectos", kwargs={"workspace_id": self.kwargs["workspace_id"]}
        )


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/eliminar_proyecto.html"
    context_object_name = "proyecto"

    def get_queryset(self):
        queryset = super().get_queryset()
        workspace = get_object_or_404(
            Workspace, id=self.kwargs["workspace_id"], owner=self.request.user
        )
        return queryset.filter(workspace=workspace)

    def get_success_url(self):
        return reverse_lazy(
            "listar_proyectos", kwargs={"workspace_id": self.kwargs["workspace_id"]}
        )
