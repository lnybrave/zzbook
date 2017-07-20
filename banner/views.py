# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from banner.models import Banner
from banner.serializers import BannerSerializer

logger = logging.getLogger(__name__)


class BannerViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = None

    @list_route(methods=['get'])
    def bookshelf(self, request):
        data_set = self.get_queryset().filter(type=2)
        serializer = BannerSerializer(data_set, many=True)
        return Response(serializer.data)
