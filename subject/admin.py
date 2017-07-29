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

    list_display = ['name', 'desc', 'code', 'icon_img', 'is_recommend', 'status']
    readonly_fields = ('icon_img',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """

    list_display = ['name', 'desc', 'sort']

    filter_horizontal = ['books']


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    model = Ranking
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']

    filter_horizontal = ['books']


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    model = Classification
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']

    filter_horizontal = ['books']
