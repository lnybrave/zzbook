# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Classification, Ranking, Topic, Column, ColumnConfig
from subject.serializers import ClassificationSerializer, RankingItemSerializer, ColumnSerializer, \
    TopicSerializer, RankingItemWithBooksSerializer, TopicDetailSerializer, \
    ColumnConfigSerializer


class TopicViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    专题
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = None


class TopicDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    专题详情
    """
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    pagination_class = None


class ColumnViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    栏目
    """
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ColumnSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class RecommendationView(generics.ListAPIView):
    """
    精选栏目
    """
    queryset = ColumnConfig.objects.all()
    serializer_class = ColumnConfigSerializer

    def get_queryset(self):
        item = Column.objects.all()[0]
        if item is not None:
            return ColumnConfig.objects.filter(item=item).all()
        return super(RecommendationView, self).get_queryset()


class ColumnDetailViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    栏目详情
    """
    queryset = ColumnConfig.objects.all()
    serializer_class = ColumnConfigSerializer

    def get_queryset(self):
        item = self.kwargs.get('id', None)
        if item is not None:
            return ColumnConfig.objects.filter(item=item).all()
        return super(ColumnDetailViewSet, self).get_queryset()


class ClassificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    默认或子项分类列表
    """
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None
    filter_fields = ['parent']

    def get_queryset(self):
        parent = self.request.query_params.get('parent', None)
        if parent is None:
            qs = Classification.objects.filter(level=0)
            if qs.count() != 0:
                parent = qs[0]
                return Classification.objects.filter(parent=parent)
        return super(ClassificationViewSet, self).get_queryset()


class ClassificationBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    分类图书列表
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        first_id = self.kwargs.get('parent', None)
        second_id = self.kwargs.get('id', None)
        param = {}
        if first_id is not None:
            param['classificationconfig__item__parent'] = first_id
        if second_id is not None:
            param['classificationconfig__item'] = second_id
        return Book.objects.filter(**param).distinct()


class RankingViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    默认或子项排行列表
    """
    queryset = Ranking.objects.all()
    serializer_class = RankingItemSerializer
    pagination_class = None
    filter_fields = ['parent']

    def get_queryset(self):
        parent = self.request.query_params.get('parent', None)
        if parent is None:
            qs = Ranking.objects.filter(level=0)
            if qs.count() != 0:
                parent = qs[0]
                return Ranking.objects.filter(parent=parent)
        return super(RankingViewSet, self).get_queryset()


class RankingWithBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    排行子项列表（附带前几本图书）
    """
    queryset = Ranking.objects.all()
    serializer_class = RankingItemWithBooksSerializer
    pagination_class = None
    filter_fields = ['parent']

    def get_queryset(self):
        parent = self.request.query_params.get('parent', None)
        if parent is None:
            qs = Ranking.objects.filter(level=0)
            if qs.count() != 0:
                parent = qs[0]
                return Ranking.objects.filter(parent=parent)
        return super(RankingWithBooksViewSet, self).get_queryset()


class RankingBooksViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    排行图书列表
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        first_id = self.kwargs.get('id', None)
        param = {}
        if first_id is not None:
            param['rankingconfig__item'] = first_id
        return Book.objects.filter(**param).distinct()
