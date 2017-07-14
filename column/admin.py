# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from column.models import Column, Topic


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    """
    栏目
    """

    list_display = ['name', 'desc', 'sort']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """

    list_display = ['name', 'desc', 'column_name', 'sort']
