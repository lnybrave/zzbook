# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from column.models import Column


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'
