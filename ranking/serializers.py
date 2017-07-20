# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.serializers import BookSerializer
from ranking.models import Ranking


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
