# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from banner.models import Banner
from banner.serializers import BannerSerializer

logger = logging.getLogger(__name__)


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    @list_route(methods=['get'])
    def test(self, request):
        return Response(status=status.HTTP_200_OK)
