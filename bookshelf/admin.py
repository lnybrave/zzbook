# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from bookshelf.models import Bookshelf


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    """
    书架
    """

    list_display = ['book_name', 'author_names', 'sort']
