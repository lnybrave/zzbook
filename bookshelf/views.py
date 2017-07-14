# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets

from bookshelf.models import Bookshelf
from bookshelf.serializers import BookshelfSerializer


class BookshelfViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
