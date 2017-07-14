# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import serializers

from ranking.models import Ranking


class RankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        fields = '__all__'
