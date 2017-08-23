# !/usr/bin/python
# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from subject.models import Topic, ColumnConfig, Classification, Ranking, Column
from utils import storage
from utils.const import CHOICE_STATUS


class Menu(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    is_recommend = models.BooleanField(default=False, verbose_name=u'精选')
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, storage=storage.ImageStorage())
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    topic = models.ForeignKey(Topic, blank=True, null=True, verbose_name=u'专题')
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name=u'栏目')
    ranking = models.ForeignKey(Ranking, blank=True, null=True, verbose_name=u'排行')
    classification = models.ForeignKey(Classification, blank=True, null=True, verbose_name=u'分类')

    class Meta:
        db_table = "t_menu"
        verbose_name = u"菜单"
        verbose_name_plural = u"菜单"
        ordering = ('sort',)

    def __unicode__(self):
        return self.name

    def icon_img(self):
        if self.icon:
            return '<img src="/media/%s" />' % self.icon
        else:
            return '(no image)'

    icon_img.short_description = 'Thumb'
    icon_img.allow_tags = True

    def type(self):
        if self.topic:
            return 0
        if self.column:
            return 1
        if self.ranking:
            return 2
        if self.classification:
            return 3
        else:
            return 0

    type.short_description = 'type'
    type.allow_tags = True
