# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.contrib import admin
from suit.admin import SortableModelAdmin

from banner.models import Banner


@admin.register(Banner)
class BannerAdmin(SortableModelAdmin):
    """
    广告
    """

    list_display = ['name', 'type', 'order', 'desc', 'banner_img']
