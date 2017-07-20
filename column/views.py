# !/user/bin/python
# -*- coding=utf-8 -*-
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from column.models import Column, Topic
from column.serializers import ColumnSerializer, TopicSerializer


class ColumnViewSet(ReadOnlyModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    pagination_class = None


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
