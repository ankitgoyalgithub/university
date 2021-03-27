import logging

from rest_framework import generics

from courses.models import Course, CourseInstructor
from courses.serializers import CourseInstructorSerializer, CourseSerializer

logger = logging.getLogger("__name__")


class CourseListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseInstructorListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CourseInstructorSerializer
    queryset = CourseInstructor.objects.all()
