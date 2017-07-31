# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    图书
    """

    list_display = ['name', 'author_names', 'cover_img', 'status', 'brief', 'chapter_size', 'score', 'charge_mode',
                    'price']

    filter_horizontal = ['author']
