# !/user/bin/python
# -*- coding=utf-8 -*-
from rest_framework import viewsets

from classification.models import Classification
from classification.serializers import ClassificationSerializer


class ClassificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None
