# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models


class HotWordType(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"名称")
    code = models.CharField(max_length=32, unique=True, verbose_name=u"唯一码")

    class Meta:
        db_table = "t_hot_word_type"
        verbose_name = u"关键字类型表"
        verbose_name_plural = u"关键字类型表"

    def __unicode__(self):
        return self.name


class HotWord(models.Model):
    key = models.CharField(max_length=64, verbose_name=u"关键字")
    type = models.ForeignKey(HotWordType, verbose_name=u"类型")

    class Meta:
        db_table = "t_hot_word"
        verbose_name = u"关键字表"
        verbose_name_plural = u"关键字表"

    def __unicode__(self):
        return self.key

    def hot_word_type(self):
        return self.type.name

    hot_word_type.short_description = u"类型"

    def get_format_dict(self):
        return {
            "key": self.key,
            "type": self.type
        }
