from django.db import models
from django.conf import settings


# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workspaces"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "name"], name="unique_workspace_name_per_user"
            )
        ]

    def __str__(self):
        return self.name
