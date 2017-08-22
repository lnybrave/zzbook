# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    图书详情
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = None
