# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route, api_view, detail_route
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Topic, Classification, Ranking, Subject
from subject.serializers import TopicSerializer, ClassificationSerializer, ClassificationDetailSerializer, \
    RankingDetailSerializer, RankingSerializer, SubjectSerializer, RankingFirstSerializer
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


class ColumnTopicViewSet(mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ClassificationViewSet(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = ClassificationSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def detail(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = Book.objects.filter(classification_books=instance).distinct()
        serializer = BookSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def all(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = Book.objects.filter(classification_books__parent=instance).distinct()
        serializer = BookSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


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
