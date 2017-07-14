# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from books.models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    作者
    """

    list_display = ['name', 'brief', 'email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    图书
    """

    list_display = ['name', 'brief', 'author_names']

    filter_horizontal = ['author']
