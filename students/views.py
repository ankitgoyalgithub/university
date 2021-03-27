import logging

from rest_framework import generics

from students.models import Student
from students.serializer import StudentSerializer

logger = logging.getLogger("__name__")


class StudentListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
