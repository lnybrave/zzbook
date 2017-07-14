# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets

from ranking.models import Ranking
from ranking.serializers import RankingSerializer


class RankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
