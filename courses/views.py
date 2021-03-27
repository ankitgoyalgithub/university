import logging

from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

logger = logging.getLogger("__name__")


class CourseListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
