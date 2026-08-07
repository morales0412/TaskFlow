from django.forms import ModelForm
from .models import Workspace
from django import forms


class WorkspaceForm(ModelForm):
    class Meta:
        model = Workspace
        fields = ["name", "description"]
        labels = {
            "name": "nombre workspace",
            "description": "descripción workspace",
        }
        error_messages = {
            "name": {
                "required": "El nombre del workspace es obligatorio.",
                "max_length": "descripcion muy larga, máximo 100 caracteres.",
            }
        }
        widgets = {
            "name": forms.TextInput(placeholder="workspace name"),
            "description": forms.Textarea(
                attrs={"placeholder": "workspace description"}
            ),
        }
