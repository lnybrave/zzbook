# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from bookshelf.models import Bookshelf


class BookshelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookshelf
        fields = '__all__'
