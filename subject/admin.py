# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import TreeRelatedFieldListFilter

from subject.models import Subject, Topic, Ranking, Classification


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    频道
    """

    list_display = ['name', 'desc', 'sort']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """

    list_display = ['name', 'desc', 'sort']


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    model = Ranking
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    model = Classification
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']
