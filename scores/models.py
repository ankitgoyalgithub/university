import uuid

from django.db import models

from exams.models import Exam
from students.models import Student


class Score(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(
        Student,
        related_name="students_scores",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    exam = models.ForeignKey(
        Exam,
        related_name="exams_scores",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    score_obtained = models.FloatField(default=0.0)
