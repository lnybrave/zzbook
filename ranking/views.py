# !/usr/bin/python
# -*- coding=utf-8 -*-
from rest_framework.viewsets import ReadOnlyModelViewSet

from ranking.models import Ranking
from ranking.serializers import RankingSerializer


class RankingViewSet(ReadOnlyModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    pagination_class = None
