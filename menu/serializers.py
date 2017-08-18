# !/usr/bin/python
# -*- coding=utf-8 -*-
from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'icon')
