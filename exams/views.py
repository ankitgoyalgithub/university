import logging

from rest_framework import generics

from exams.models import Exam
from exams.serializers import ExamSerializer

logger = logging.getLogger("__name__")


class ExamListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
