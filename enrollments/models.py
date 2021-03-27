import uuid

from django.db import models

from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(
        Student,
        related_name="student_enrollments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Course,
        related_name="course_enrollments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
