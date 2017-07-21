# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from account.models import User


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'avatar')
