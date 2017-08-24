# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from account.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, help_text='用户名')
    password = serializers.CharField(max_length=30, help_text='密码')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'full_name')


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'avatar')
