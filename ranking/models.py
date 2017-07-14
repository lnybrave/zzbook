# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models


class Ranking(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')

    class Meta:
        db_table = "t_ranking"
        verbose_name = u"排行表"
        verbose_name_plural = u"排行表"

    def get_format_dict(self):
        return {
            "name": self.name
        }
