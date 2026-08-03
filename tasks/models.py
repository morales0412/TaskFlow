from django.db import models
from projects.models import Project
# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("IN_PROGRESS", "En progreso"),
        ("COMPLETED", "Completada"),
    ]
    IMPORTANT_CHOICES = [
        ("HIGH", "Alta"),
        ("MEDIUM", "Media"),
        ("LOW", "Baja"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    importance = models.CharField(
        max_length=10, choices=IMPORTANT_CHOICES, default="MEDIUM"
    )
    limit_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.name
