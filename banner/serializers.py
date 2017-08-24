# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from banner.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    book = PrimaryKeyRelatedField(read_only=True)
    topic = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Banner
        fields = ('name', 'desc', 'img', 'type', 'book', 'topic', 'url')
