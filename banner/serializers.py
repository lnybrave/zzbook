# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from banner.models import Banner


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'
