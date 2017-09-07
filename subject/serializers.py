# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.models import Book
from books.serializers import BookSerializer
from subject.models import Classification, Ranking, Topic, Column, ColumnConfig


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'desc', 'type')


class TopicDetailSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField('get_all_books')

    class Meta:
        model = Topic
        fields = ('id', 'name', 'desc', 'type', 'books')

    def get_all_books(self, obj):
        indicators = Book.objects.filter(topicconfig__item=obj).all()
        return BookSerializer(indicators, many=True).data


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name', 'desc')


class ColumnConfigSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    topic = TopicDetailSerializer()

    class Meta:
        model = ColumnConfig
        fields = ('book', 'topic')


class ColumnDetailSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('get_all_books')

    class Meta:
        model = Column
        fields = ('id', 'name', 'desc', 'items')

    def get_all_books(self, obj):
        indicators = ColumnConfig.objects.filter(item=obj).all()
        return ColumnConfigSerializer(indicators, many=True).data


class ClassificationSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Classification
        fields = ('id', 'name', 'icon', 'children')


# class ClassificationDetailSerializer(serializers.ModelSerializer):
#     """
#     分类详情
#     """
#     books = serializers.SerializerMethodField('get_all_books')
#
#     class Meta:
#         model = Classification
#         fields = ('id', 'name', 'books')
#
#     def get_all_books(self, obj):
#         indicators = Book.objects.filter(classificationconfig__item=obj).all()
#         return BookSerializer(indicators, many=True).data


class RankingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('id', 'name')


# noinspection PyMethodMayBeStatic
class RankingItemWithBooksSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'books')

    def get_books(self, obj):
        return BookSerializer(obj.get_top_three_books(), many=True).data
