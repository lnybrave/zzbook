# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models


class SearchWord(models.Model):
    word = models.CharField(max_length=64, unique=True, verbose_name=u"关键字")
    is_hot = models.BooleanField(default=False, verbose_name=u"热词")
    count = models.IntegerField(default=1, verbose_name=u"次数")

    class Meta:
        db_table = "t_hot_word"
        verbose_name = u"关键字"
        verbose_name_plural = u"关键字"

    def __unicode__(self):
        return self.word
