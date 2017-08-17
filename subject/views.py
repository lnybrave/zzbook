# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Topic, Classification, Ranking, Subject
from subject.serializers import TopicSerializer, ClassificationSerializer, RankingDetailSerializer, RankingSerializer, \
    SubjectSerializer, RankingFirstSerializer
from utils.const import SUBJECT_COLUMN, SUBJECT_CODE_RECOMMENDATION


class SubjectViewSet(mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @list_route(methods=['get'])
    def recommendation(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(is_recommend=True))
        serializer = SubjectSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class ColumnViewSet(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Subject.objects.filter(type=SUBJECT_COLUMN).all()
    serializer_class = SubjectSerializer

    def retrieve(self, request, *args, **kwargs):
        obj_subject = self.get_object()
        queryset = Topic.objects.filter(subject=obj_subject)
        serializer = TopicSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @list_route(methods=['get'])
    def recommendation(self, request, *args, **kwargs):
        obj_subject = None
        qs = Subject.objects.filter(code=SUBJECT_CODE_RECOMMENDATION)
        if qs.count() != 0:
            obj_subject = qs[0]
        if obj_subject is not None:
            queryset = Topic.objects.filter(subject=obj_subject)
            serializer = TopicSerializer(queryset, many=True, context=self.get_serializer_context())
            return Response(serializer.data)
        return Response(status=HTTP_404_NOT_FOUND)


class ColumnTopicViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ClassificationViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    分类列表
    """
    queryset = Classification.objects.filter(level=0).all()
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
