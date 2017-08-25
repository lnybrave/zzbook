# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableTabularInline

from subject.models import Topic, Ranking, Classification, ColumnConfig, Column, ClassificationConfig, RankingConfig, \
    TopicConfig


class TopicInline(SortableTabularInline):
    model = TopicConfig
    extra = 0
    fk_name = 'item'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """
    list_display = ['name', 'desc', 'type', 'status']

    exclude = ['del_flag']

    search_fields = ['name']

    inlines = [TopicInline]


class ColumnInline(SortableTabularInline):
    model = ColumnConfig
    extra = 0
    fk_name = 'item'


@admin.register(Column)
class ColumnAdmin(MPTTModelAdmin):
    """
    栏目
    """
    list_display = ['name', 'order']

    exclude = ['del_flag']

    inlines = [ColumnInline]


class ClassificationInline(SortableTabularInline):
    model = ClassificationConfig
    extra = 0
    fk_name = 'item'


@admin.register(Classification)
class ClassificationAdmin(MPTTModelAdmin):
    """
    分类
    """
    list_display = ['name', 'icon_img', 'status', 'sort']

    readonly_fields = ('icon_img',)

    exclude = ['del_flag']

    search_fields = ['name']

    inlines = [ClassificationInline]


class RankingInline(SortableTabularInline):
    model = RankingConfig
    extra = 0
    fk_name = 'item'


@admin.register(Ranking)
class RankingAdmin(MPTTModelAdmin):
    """
    排行
    """

    list_display = ['name', 'status', 'sort']

    exclude = ['del_flag']

    search_fields = ['name']

    inlines = [RankingInline]
