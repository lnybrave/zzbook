# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from books.models import Book


class Bookshelf(models.Model):
    """
    书架
    """
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    book = models.OneToOneField(Book, primary_key=True)

    class Meta:
        db_table = "t_bookshelf"
        verbose_name = u"书架表"
        verbose_name_plural = u"书架表"

    def __unicode__(self):
        return self.book.name

    def book_name(self):
        return self.book.name

    book_name.short_description = u"书名"

    def author_names(self):
        return self.book.author_names()

    author_names.short_description = u"作者"
