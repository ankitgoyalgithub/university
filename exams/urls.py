from django.urls import path

from exams import views

urlpatterns = [
    path("", views.ExamListCreateView.as_view(), name="exam_create_list"),
]
