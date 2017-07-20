# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import TreeRelatedFieldListFilter

from ranking.models import Ranking


@admin.register(Ranking)
class MyModelAdmin(admin.ModelAdmin):
    model = Ranking
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']
