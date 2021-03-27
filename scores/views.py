import logging

from rest_framework import generics

from scores.models import Score
from scores.serializer import ScoreSerializer

logger = logging.getLogger("__name__")


class ScoreListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
