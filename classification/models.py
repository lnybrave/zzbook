# !/user/bin/python
# -*- coding=utf-8 -*-
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from books.models import Book


class Classification(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'名称')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    books = models.ManyToManyField(Book, blank=True, related_name='classification_books')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = "t_classification"
        verbose_name = u"分类"
        verbose_name_plural = u"分类"

    def __unicode__(self):
        return self.name
