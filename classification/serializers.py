# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from books.serializers import BookSerializer
from classification.models import Classification


class ClassificationSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Classification
        fields = ('id', 'name', 'parent', 'children', 'books')
