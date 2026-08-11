from .models import Task
from django import forms
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "importance", "limit_date"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "nombre"}),
            "description": forms.Textarea(attrs={"placeholder": "descripcion"}),
            "limit_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "name": "nombre tarea",
            "description": "descripción tarea",
            "status": "estado",
            "importance": "importancia",
            "limit_date": "fecha límite",
        }

        error_messages = {
            "name": {
                "required": "El nombre de la tarea es obligatorio.",
                "max_length": "El nombre debe tener un max de 100 caracteres.",
            },
            "description": {
                "max_length": "La descripción debe tener un max de 500 caracteres."
            },
            "limit_date": {"invalid": "La fecha límite no es válida."},
        }
