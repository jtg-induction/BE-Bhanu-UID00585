from users.models import CustomUser

from django.db import models


class Todo(models.Model):
    """
    create todo model
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
