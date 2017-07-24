# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from subject.models import Topic, Classification, Ranking, Subject
from subject.serializers import TopicSerializer, ClassificationSerializer, ClassificationDetailSerializer, \
    RankingDetailSerializer, RankingSerializer, SubjectSerializer
from utils.const import SUBJECT_COLUMN


class SubjectViewSet(mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @list_route(methods=['get'])
    def recommend(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(type=SUBJECT_COLUMN))
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
        if Subject.objects.filter(code="recommendation").count() != 0:
            obj_subject = Subject.objects.filter(code="recommendation")[0]
        if obj_subject is not None:
            queryset = Topic.objects.filter(subject=obj_subject)
            serializer = TopicSerializer(queryset, many=True, context=self.get_serializer_context())
            return Response(serializer.data)
        return Response(status=HTTP_404_NOT_FOUND)


class ColumnTopicViewSet(mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ClassificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level=0))
        serializer = ClassificationSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClassificationDetailSerializer(instance, context=self.get_serializer_context())
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
        serializer = RankingDetailSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
