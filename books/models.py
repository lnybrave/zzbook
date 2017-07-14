# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    brief = models.CharField(max_length=256, verbose_name=u'简介')
    email = models.EmailField()

    class Meta:
        db_table = "t_author"
        verbose_name = u"作者表"
        verbose_name_plural = u"作者表"

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    brief = models.CharField(max_length=256, verbose_name=u'简介')
    author = models.ManyToManyField(Author)

    class Meta:
        db_table = "t_book"
        verbose_name = u"图书表"
        verbose_name_plural = u"图书表"

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
        verbose_name = u"目录表"
        verbose_name_plural = u"目录表"
