from django.urls import path

from instructors import views

urlpatterns = [
    path("", views.InstructorListCreateView.as_view(), name="instructor_create_list"),
]
