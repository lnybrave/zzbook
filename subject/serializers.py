# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.serializers import BookSerializer
from subject.models import Classification, Ranking, Topic, Column


class TopicSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'desc', 'type', 'books')


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = ('id', 'name', 'desc')


class ColumnDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Column
        fields = ('id', 'name', 'desc', 'children', 'books', 'topics')


class ClassificationSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Classification
        fields = ('id', 'name', 'icon', 'children')


class ClassificationDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Classification
        fields = ('id', 'name', 'books')


class RankingFirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('id', 'name')


class RankingSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())
    books = BookSerializer(many=True)

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'children', 'books')


class RankingDetailSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())
    books = BookSerializer(many=True)

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'children', 'books')
