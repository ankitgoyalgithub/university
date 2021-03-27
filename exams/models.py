import uuid

from django.db import models

from courses.models import Course
from instructors.models import Instructor


class Exam(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    course = models.ForeignKey(
        Course,
        related_name="course_exams_taken",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    instructor = models.ForeignKey(
        Instructor,
        related_name="exams_taken",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
