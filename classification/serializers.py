# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.serializers import BookSerializer
from classification.models import Classification


class ClassificationSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Classification
        fields = ('id', 'name', 'children', 'books')
