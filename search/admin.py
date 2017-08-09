# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from search.models import SearchWord


@admin.register(SearchWord)
class SearchWordAdmin(admin.ModelAdmin):
    """
    搜索
    """

    list_display = ['word', 'is_hot', 'count']
