# !/usr/bin/python
# -*- coding=utf-8 -*-
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ranking.models import Ranking
from ranking.serializers import RankingSerializer, RankingDetailSerializer


class RankingViewSet(ReadOnlyModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingDetailSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = RankingSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RankingDetailSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
