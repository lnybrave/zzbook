# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

import coreapi
from rest_framework import mixins, filters
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from search.models import SearchWord
from search.serializers import SearchWordSerializer

logger = logging.getLogger(__name__)


class SearchWordViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = SearchWord.objects.filter(is_hot=True).all()
    serializer_class = SearchWordSerializer
    pagination_class = None


class WordFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        content = request.query_params.get('word', None)
        if content is not None:
            return SearchWord.objects.filter(word__contains=content)
        return queryset

    def get_schema_fields(self, view):
        return coreapi.Field(name='word', required=False, location='query')


class SearchSuggestViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = SearchWord.objects.all()
    serializer_class = SearchWordSerializer
    pagination_class = None

    # 对list有效
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['word']

    def get_queryset(self):
        content = self.request.query_params.get('word', None)
        if content is not None:
            return SearchWord.objects.filter(word__contains=content)
        return self.queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class SearchTopViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = None

    def get_queryset(self):
        count = self.kwargs.get('count', 5)
        if count is not None:
            return Book.objects.order_by('-click_amount')[:count]
        return self.queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class SearchBookViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('name',)

    def list(self, request, *args, **kwargs):
        content = request.query_params[filters.SearchFilter.search_param]
        if content is None:
            return Response(status=HTTP_400_BAD_REQUEST)

        if SearchWord.objects.filter(word=content).count() == 0:
            sw = SearchWord(word=content, is_hot=False)
            sw.save()
        else:
            sw = SearchWord.objects.filter(word=content).get()
            sw.count += 1
            sw.save()

        return super(SearchBookViewSet, self).list(self, request, *args, **kwargs)
