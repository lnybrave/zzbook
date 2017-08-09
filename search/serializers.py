# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from search.models import SearchWord


class SearchWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchWord
        fields = ('word', 'count')
