# !/usr/bin/python
# -*- coding=utf-8 -*-
import logging

import django_filters
from rest_framework import mixins, filters
from rest_framework.decorators import list_route
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


class WordFilter(django_filters.rest_framework.FilterSet):
    def __init__(self):
        pass

    content = django_filters.CharFilter(name="content")

    class Meta:
        model = SearchWord
        fields = ['word']


class SearchAutoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = SearchWord.objects.all()
    serializer_class = SearchWordSerializer
    pagination_class = None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = WordFilter

    @list_route()
    def auto(self, request, *args, **kwargs):
        content = kwargs['content']
        if content is not None:
            return Response(status=HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset().filter(word__contains=content))
        serializer = self.get_serializer(queryset, many=True)
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
