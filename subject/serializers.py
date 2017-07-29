# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.serializers import BookSerializer
from models import Subject
from subject.models import Classification, Ranking, Topic


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('pk', 'name', 'desc', 'type', 'icon')


class TopicSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('pk', 'name', 'desc', 'type', 'books')


class ClassificationSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Classification
        fields = ('id', 'name', 'children')


class ClassificationDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Classification
        fields = ('id', 'name', 'books')


class RankingSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'children')


class RankingDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'books')
