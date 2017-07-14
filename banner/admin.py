# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.contrib import admin

from banner.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    """
    广告
    """

    list_display = ['name', 'desc', 'img', 'type']
