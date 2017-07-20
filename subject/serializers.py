# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from column.models import Column, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
