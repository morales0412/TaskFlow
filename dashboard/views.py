from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from projects.models import Project
from tasks.models import Task
from workspaces.models import Workspace
from django.db.models import Count


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        total_workspaces = Workspace.objects.filter(owner=usuario).count()
        total_projects = Project.objects.filter(workspace__owner=usuario).count()
        total_tareas = Task.objects.filter(project__workspace__owner=usuario).count()
        tareas = Task.objects.filter(project__workspace__owner=usuario)
        estados = (
            Task.objects.filter(project__workspace__owner=usuario)
            .values("status")
            .annotate(cantidad=Count("status"))
        )
        estado = self.request.GET.get("estado", "")
        if estado:
            tareas = tareas.filter(status=estado)
        context["total_workspaces"] = total_workspaces
        context["total_projects"] = total_projects
        context["total_tareas"] = total_tareas
        context["tareas"] = tareas
        context["estados"] = estados
        return context


# Create your views here.
