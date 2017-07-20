# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from hotword.models import HotWord
from hotword.serializers import HotWordSerializer

logger = logging.getLogger(__name__)


class HotWordViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = HotWord.objects.all()
    serializer_class = HotWordSerializer
    pagination_class = None
