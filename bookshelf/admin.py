# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from suit.admin import SortableModelAdmin

from bookshelf.models import Bookshelf


@admin.register(Bookshelf)
class BookshelfAdmin(SortableModelAdmin):
    """
    书架
    """

    list_display = ['name', 'cover_img', 'order', 'status']
