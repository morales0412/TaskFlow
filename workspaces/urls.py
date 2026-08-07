from django.urls import path
from .views import (
    WorkspaceListView,
    WorkspaceCreateView,
    WorkspaceUpdateView,
    WorkspaceDeleteView,
)

urlpatterns = [
    path("listar", WorkspaceListView.as_view(), name="listar_workspaces"),
    path("crear", WorkspaceCreateView.as_view(), name="crear_workspace"),
    path("editar/<int:pk>", WorkspaceUpdateView.as_view(), name="editar_workspace"),
    path("eliminar/<int:pk>", WorkspaceDeleteView.as_view(), name="eliminar_workspace"),
]
