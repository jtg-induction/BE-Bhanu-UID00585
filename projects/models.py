from django.db import models
from .constants import STATUS_CHOICES

from users.models import CustomUser

"""creating a models for project  """

class Project(models.Model):
    """
    Represents a project that can have multiple members.
    """

    members = models.ManyToManyField(
        CustomUser, through="ProjectMember", related_name="projects"
    )
    name = models.CharField(max_length=100, unique=True)
    max_members = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    """
    Represents the association between a project and its members.
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Meta:
    Constraints = [
        models.UniqueConstraint(
            fields=["member", "project"],
            name="unique_enrollment",
        )
    ]
