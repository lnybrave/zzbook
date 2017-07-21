# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from search.models import SearchWord
from search.serializers import SearchWordSerializer

logger = logging.getLogger(__name__)


class SearchWordViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = SearchWord.objects.all()
    serializer_class = SearchWordSerializer
    pagination_class = None


class SearchBookViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('name',)
