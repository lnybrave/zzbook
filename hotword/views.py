# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import viewsets

from hotword.models import HotWord
from hotword.serializers import HotWordSerializer

logger = logging.getLogger(__name__)


class HotWordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HotWord.objects.all()
    serializer_class = HotWordSerializer
