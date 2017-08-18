# !/usr/bin/python
# -*- coding=utf-8 -*-
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from recommend.models import Recommend
from recommend.serializers import RecommendSerializer


class RecommendViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    精选列表
    """
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer
