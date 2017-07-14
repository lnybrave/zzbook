# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from hotword.models import HotWord, HotWordType


class HotWordTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotWordType
        fields = '__all__'


class HotWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotWord
        fields = '__all__'
