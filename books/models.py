# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from account.models import User


class Book(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=u'ID')
    name = models.CharField(max_length=128, verbose_name=u'名称')
    brief = models.CharField(max_length=256, verbose_name=u'简介')
    author = models.ManyToManyField(User, blank=True)

    class Meta:
        db_table = "t_book"
        verbose_name = u"图书"
        verbose_name_plural = u"图书"

    def __unicode__(self):
        return self.name

    def author_names(self):
        return [author.name for author in self.author.filter(book=self)]

    author_names.short_description = u"作者"


class Content(models.Model):
    book = models.ForeignKey(Book)
    prev_cid = models.IntegerField(default=0, verbose_name=u"上一章id")
    next_cid = models.IntegerField(default=0, verbose_name=u"下一章id")

    class Meta:
        db_table = "t_content"
        verbose_name = u"目录"
        verbose_name_plural = u"目录"
