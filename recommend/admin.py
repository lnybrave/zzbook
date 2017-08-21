# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.contrib import admin

from recommend.models import Recommend


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    """
    精选
    """
    list_display = ['title', 'type', 'status']
