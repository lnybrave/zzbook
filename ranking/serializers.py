# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from books.serializers import BookSerializer
from ranking.models import Ranking


class RankingSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Ranking
        fields = ('id', 'name', 'parent', 'children', 'books')
