# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from subject.models import Topic, Ranking, Classification, Column


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """
    list_display = ['name', 'desc', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']


@admin.register(Column)
class ColumnAdmin(MPTTModelAdmin):
    """
    栏目
    """
    list_display = ['name', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']


@admin.register(Classification)
class ClassificationAdmin(MPTTModelAdmin):
    """
    分类
    """
    list_display = ['name', 'icon_img', 'status', 'sort']

    readonly_fields = ('icon_img',)

    exclude = ['del_flag']

    filter_horizontal = ['books']


@admin.register(Ranking)
class RankingAdmin(MPTTModelAdmin):
    """
    排行
    """

    list_display = ['name', 'status', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']
