import logging

from rest_framework import generics

from instructors.models import Instructor
from instructors.serializers import InstructorSerializer

logger = logging.getLogger("__name__")


class InstructorListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
