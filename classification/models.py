# !/user/bin/python
# -*- coding=utf-8 -*-
from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')

    class Meta:
        db_table = "t_classification"
        verbose_name = u"分类表"
        verbose_name_plural = u"分类表"

    def get_format_dict(self):
        return {
            "name": self.name
        }
