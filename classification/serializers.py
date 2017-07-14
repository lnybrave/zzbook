# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from classification.models import Classification


class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__'
