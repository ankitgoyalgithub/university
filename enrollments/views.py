import logging

from rest_framework import generics

from enrollments.models import Enrollment
from enrollments.serializers import EnrollmentSerializer

logger = logging.getLogger("__name__")


class EnrollmentListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
