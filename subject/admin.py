# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from subject.models import Topic, Ranking, Classification, ColumnConfig, Column, ClassificationConfig, RankingConfig, \
    TopicConfig


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """
    list_display = ['name', 'desc', 'type', 'status']

    exclude = ['del_flag']

    search_fields = ['name']


@admin.register(TopicConfig)
class TopicConfigAdmin(admin.ModelAdmin):
    """
    专题
    """
    list_display = ['item_name', 'title', 'type', 'sort']


@admin.register(Column)
class ColumnAdmin(MPTTModelAdmin):
    """
    栏目
    """
    list_display = ['name', 'order']

    exclude = ['del_flag']


@admin.register(ColumnConfig)
class ColumnConfigAdmin(admin.ModelAdmin):
    """
    栏目
    """
    list_display = ['item_name', 'title', 'type', 'sort']


@admin.register(Classification)
class ClassificationAdmin(MPTTModelAdmin):
    """
    分类
    """
    list_display = ['name', 'icon_img', 'status', 'sort']

    readonly_fields = ('icon_img',)

    exclude = ['del_flag']

    search_fields = ['name']


@admin.register(ClassificationConfig)
class ClassificationConfigAdmin(admin.ModelAdmin):
    """
    分类
    """
    list_display = ['item_name', 'title', 'type', 'sort']


@admin.register(Ranking)
class RankingAdmin(MPTTModelAdmin):
    """
    排行
    """

    list_display = ['name', 'status', 'sort']

    exclude = ['del_flag']

    search_fields = ['name']


@admin.register(RankingConfig)
class RankingConfigAdmin(admin.ModelAdmin):
    """
    排行
    """
    list_display = ['item_name', 'title', 'type', 'sort']
