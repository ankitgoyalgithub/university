import uuid

from django.db import models


class Instructor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
