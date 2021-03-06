# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from books.models import Book
from utils.const import CHOICE_STATUS


class Bookshelf(models.Model):
    """
    书架
    """
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    book = models.OneToOneField(Book, primary_key=True)

    class Meta:
        db_table = "t_bookshelf"
        verbose_name = u"书架"
        verbose_name_plural = u"书架"
        ordering = ('order',)

    def __unicode__(self):
        return self.book.name

    def name(self):
        return self.book.name

    name.short_description = u"书名"

    def author_names(self):
        return self.book.author_names()

    author_names.short_description = u"作者"

    def cover_img(self):
        if self.book.cover:
            return '<img src="/media/%s" />' % self.book.cover
        elif self.book.cover_url:
            return '<img src="%s" />' % self.book.cover_url
        elif self.book.cover_url_small:
            return '<img src="%s" />' % self.book.cover_url_small
        else:
            return '(no image)'

    cover_img.short_description = '封面'
    cover_img.allow_tags = True
