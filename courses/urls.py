from django.urls import path

from courses import views

urlpatterns = [
    path("", views.CourseListCreateView.as_view(), name="course_create_list"),
]
