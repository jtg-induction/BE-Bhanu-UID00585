from django.db import models

from users.models import CustomUser


class Project(models.Model):
    STATUS_CHOICES = [
        (0, "To be started"),
        (1, "In progress"),
        (2, "Completed"),
    ]
    members = models.ManyToManyField(
        CustomUser, through="ProjectMember", related_name="projects"
    )
    name = models.CharField(max_length=100, unique=True)
    max_members = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )  # (fk to User model - use AUTH_USER_MODEL from settings)


class Meta:
    Constraints = [
        models.UniqueConstraint(
            fields=["member", "project"],
            name="unique_enrollment",
        )
    ]

    # Add string representation for this model with project name and user email/first name.
