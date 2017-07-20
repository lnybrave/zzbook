# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from column.models import Column, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Column
        fields = ('name', 'desc', 'topics')
