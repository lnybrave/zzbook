# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from books.models import Book
from subject.models import Subject


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    type = models.IntegerField(default=0, verbose_name=u'类型')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    book = models.ManyToManyField(Book)

    class Meta:
        db_table = "t_topic"
        verbose_name = u"专题"
        verbose_name_plural = u"专题"

    def __unicode__(self):
        return self.name

    def column_name(self):
        return self.column.name

    column_name.short_description = u"栏目"


class Column(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    subject = models.ForeignKey(Subject)
    topics = models.ManyToManyField(Topic, related_name='topics')

    class Meta:
        db_table = "t_column"
        verbose_name = u"栏目"
        verbose_name_plural = u"栏目"

    def __unicode__(self):
        return self.name

    def get_format_dict(self):
        return {
            "id": self.pk,
            "name": self.name,
            "desc": self.desc,
        }
