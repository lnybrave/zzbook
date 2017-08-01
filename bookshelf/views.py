# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from books.models import Book
from books.serializers import BookSerializer


class BookshelfViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Book.objects.filter(bookshelf__isnull=False).order_by('-bookshelf__sort')
    serializer_class = BookSerializer
    pagination_class = None
