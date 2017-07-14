# !/user/bin/python
# -*- coding=utf-8 -*-
from rest_framework import viewsets

from column.models import Column
from column.serializers import ColumnSerializer


class ColumnViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
