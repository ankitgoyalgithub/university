from django.contrib import admin

from courses.models import Course, CourseInstructor

admin.site.register(Course)
admin.site.register(CourseInstructor)
