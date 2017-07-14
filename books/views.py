# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
