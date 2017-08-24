# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.contrib import admin
from suit.admin import SortableModelAdmin

from recommend.models import Recommend


@admin.register(Recommend)
class RecommendAdmin(SortableModelAdmin):
    """
    精选
    """
    list_display = ['title', 'type', 'order', 'status']
