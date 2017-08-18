# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Classification, Ranking, Column
from subject.serializers import ClassificationSerializer, RankingDetailSerializer, RankingSerializer, \
    RankingFirstSerializer, ColumnSerializer, ColumnDetailSerializer


class ColumnViewSet(ReadOnlyModelViewSet):
    """
    栏目
    """
    queryset = Column.objects.filter(level=0).all()
    serializer_class = ColumnSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        kwargs['context'] = self.get_serializer_context()
        serializer = ColumnSerializer(queryset, many=True, *args, **kwargs)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ColumnDetailSerializer(instance)
        return Response(serializer.data)


class ClassificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    分类列表
    """
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None


class ClassificationBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    分类详情
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        first_id = int(self.kwargs.get('first_id', '0'))
        second_id = int(self.kwargs.get('second_id', '0'))
        param = {}
        if first_id != 0:
            param['classification_books__parent'] = first_id
        if second_id != 0:
            param['classification_books'] = second_id
        return Book.objects.filter(**param).distinct()


class RankingViewSet(ReadOnlyModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingDetailSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = RankingSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RankingSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)

    @list_route(methods=['get'])
    def first(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = RankingFirstSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
