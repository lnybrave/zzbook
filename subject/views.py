# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Classification, Ranking, Column, Topic
from subject.serializers import ClassificationSerializer, RankingItemSerializer, ColumnSerializer, \
    ColumnDetailSerializer, TopicSerializer, RankingItemWithBooksSerializer


class TopicViewSet(ReadOnlyModelViewSet):
    """
    专题
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = None


class ColumnViewSet(ReadOnlyModelViewSet):
    """
    栏目
    """
    queryset = Column.objects.filter(level=0).all()
    serializer_class = ColumnSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ColumnSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ColumnDetailSerializer(instance)
        return Response(serializer.data)


class ClassificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    默认一级菜单列表
    """
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None

    def get_queryset(self):
        p = Classification.objects.filter(level=0)[0]
        return super(ClassificationViewSet, self).get_queryset().filter(parent=p)


class ClassificationItemViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    一级或子项菜单列表
    """
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None

    def get_queryset(self):
        classification_id = int(self.kwargs.get('id', '0'))
        return super(ClassificationItemViewSet, self).get_queryset().filter(parent=classification_id)


class ClassificationBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    图书列表
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        first_id = int(self.kwargs.get('parent', '0'))
        second_id = int(self.kwargs.get('id', '0'))
        param = {}
        if first_id != 0:
            param['classification_books__parent'] = first_id
        if second_id != 0:
            param['classification_books'] = second_id
        return Book.objects.filter(**param).distinct()


class RankingViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    默认一级菜单列表
    """
    queryset = Ranking.objects.all()
    serializer_class = RankingItemSerializer
    pagination_class = None

    def get_queryset(self):
        p = Ranking.objects.filter(level=0)[0]
        return super(RankingViewSet, self).get_queryset().filter(parent=p)


class RankingItemViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    一级或子项菜单列表
    """
    queryset = Ranking.objects.all()
    serializer_class = RankingItemSerializer
    pagination_class = None

    def get_queryset(self):
        ranking_id = int(self.kwargs.get('id', '0'))
        return super(RankingItemViewSet, self).get_queryset().filter(parent=ranking_id)

    @list_route(methods=['get'])
    def with_books(self, request, *args, **kwargs):
        """
        子项列表，附带前几名图书
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = RankingItemWithBooksSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class RankingItemBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    图书列表
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        first_id = int(self.kwargs.get('id', '0'))
        param = {}
        if first_id != 0:
            param['ranking_books'] = first_id
        return Book.objects.filter(**param).distinct()
