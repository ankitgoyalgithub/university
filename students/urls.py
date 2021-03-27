from django.urls import path

from students import views

urlpatterns = [
    path("", views.StudentListCreateView.as_view(), name="student_create_list"),
]
