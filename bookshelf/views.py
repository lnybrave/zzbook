# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from bookshelf.models import Bookshelf
from bookshelf.serializers import BookshelfSerializer


class BookshelfViewSet(mixins.ListModelMixin, GenericViewSet):
    # 联表查询
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
    pagination_class = None
