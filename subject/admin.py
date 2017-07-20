# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from subject.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    频道
    """

    list_display = ['name', 'desc', 'sort']
