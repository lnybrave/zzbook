# !/usr/bin/python
# -*- coding=utf-8 -*-
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from recommend.models import Recommend
from recommend.serializers import RecommendSerializer
from utils.const import STATUS_ON


class RecommendationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    精选
    """
    queryset = Recommend.objects.filter(status=STATUS_ON)
    serializer_class = RecommendSerializer
