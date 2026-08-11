from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path(
        "workspaces/<int:workspace_id>/",
        ProjectListView.as_view(),
        name="listar_proyectos",
    ),
    path(
        "workspaces/crear/<int:workspace_id>/",
        ProjectCreateView.as_view(),
        name="crear_proyecto",
    ),
    path(
        "workspaces/<int:workspace_id>/editar/<int:pk>/",
        ProjectUpdateView.as_view(),
        name="editar_proyecto",
    ),
    path(
        "wokspaces/<int:workspace_id>/eliminar/<int:pk>/",
        ProjectDeleteView.as_view(),
        name="eliminar_proyecto",
    ),
]
