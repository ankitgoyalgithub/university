from django.urls import path

from scores import views

urlpatterns = [
    path("", views.ScoreListCreateView.as_view(), name="score_create_list"),
]
