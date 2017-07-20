# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from books.serializers import BookSerializer
from column.models import Column, Topic


class TopicSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('pk', 'name', 'desc', 'type', 'is_recommend', 'books')


class ColumnSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Column
        fields = ('pk', 'name', 'desc', 'topics')
