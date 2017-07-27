# !/usr/bin/python
# -*- coding=utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')

    class Meta:
        db_table = "t_data"
        verbose_name = u"数据"
        verbose_name_plural = u"数据"

    def __unicode__(self):
        return self.name
