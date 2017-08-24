# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from books.serializers import BookSerializer
from recommend.models import Recommend
from subject.serializers import TopicDetailSerializer


class RecommendSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    topic = TopicDetailSerializer()

    class Meta:
        model = Recommend
        fields = ('id', 'book', 'topic')
