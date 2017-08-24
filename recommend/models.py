# !/usr/bin/python
# -*- coding=utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from books.models import Book
from subject.models import Topic
from utils.const import CHOICE_STATUS


class Recommend(models.Model):
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    topic = models.ForeignKey(Topic, blank=True, null=True, verbose_name=u'专题')
    book = models.ForeignKey(Book, blank=True, null=True, verbose_name=u'图书')

    class Meta:
        db_table = "t_recommend"
        verbose_name = u"精选"
        verbose_name_plural = u"精选"
        ordering = ('order',)

    def title(self):
        if self.topic is not None:
            return self.topic.name
        if self.book is not None:
            return self.book.name
        return "no title"

    title.short_description = '名称'
    title.allow_tags = True

    def type(self):
        if self.topic is not None:
            return "专题"
        if self.book is not None:
            return "图书"
        return "unknown"
