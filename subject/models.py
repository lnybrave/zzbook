# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    code = models.CharField(max_length=64, unique=True, verbose_name=u'唯一码')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, verbose_name=u'状态')
    type = models.IntegerField(default=0, verbose_name=u'类型')

    class Meta:
        db_table = "t_subject"
        verbose_name = u"频道表"
        verbose_name_plural = u"频道表"
