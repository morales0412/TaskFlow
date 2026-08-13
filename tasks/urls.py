from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path(
        "proyecto/<int:proyecto_id>/listar/",
        TaskListView.as_view(),
        name="listar_tareas",
    ),
    path(
        "proyecto/<int:proyecto_id>/crear/",
        TaskCreateView.as_view(),
        name="crear_tarea",
    ),
    path(
        "proyecto/<int:proyecto_id>/editar/<int:pk>/",
        TaskUpdateView.as_view(),
        name="editar_tarea",
    ),
    path(
        "proyecto/<int:proyecto_id>/eliminar/<int:pk>/",
        TaskDeleteView.as_view(),
        name="eliminar_tarea",
    ),
]
