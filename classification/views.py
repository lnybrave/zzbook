# !/user/bin/python
# -*- coding=utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response

from classification.models import Classification
from classification.serializers import ClassificationSerializer, ClassificationDetailSerializer


class ClassificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = ClassificationSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClassificationDetailSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
