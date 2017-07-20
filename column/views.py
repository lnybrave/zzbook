# !/user/bin/python
# -*- coding=utf-8 -*-
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from column.models import Column, Topic
from column.serializers import ColumnSerializer, TopicSerializer


class ColumnViewSet(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
