from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]
        labels = {
            "name": "nombre proyecto",
            "description": "descripción proyecto",
        }
        error_messages = {
            "name": {
                "required": "El nombre del proyecto es obligatorio.",
                "max_length": "descripcion muy larga, máximo 100 caracteres.",
            }
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "nombre"}),
            "description": forms.Textarea(attrs={"placeholder": "descripcion"}),
        }
