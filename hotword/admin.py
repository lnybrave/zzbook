# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from hotword.models import HotWord, HotWordType


@admin.register(HotWordType)
class HotWordTypeAdmin(admin.ModelAdmin):
    """
    搜索分类
    """

    list_display = ['name', 'code']


@admin.register(HotWord)
class HotWordAdmin(admin.ModelAdmin):
    """
    搜索
    """

    list_display = ['key', 'hot_word_type']
