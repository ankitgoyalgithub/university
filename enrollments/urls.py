from django.urls import path

from enrollments import views

urlpatterns = [
    path("", views.EnrollmentListCreateView.as_view(), name="enrollment_create_list"),
]
