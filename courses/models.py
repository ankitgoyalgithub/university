import uuid

from django.db import models

from instructors.models import Instructor


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class CourseInstructor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, related_name="course_instructors", on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        Instructor,
        related_name="instructor_courses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.course.name+"---"+self.instructor.name
