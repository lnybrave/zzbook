# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from banner.models import Banner
from banner.serializers import BannerSerializer
from utils.const import STATUS_ON

logger = logging.getLogger(__name__)


class BannerViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    轮播广告
    """
    queryset = Banner.objects.filter(status=STATUS_ON).all()
    serializer_class = BannerSerializer
    pagination_class = None
