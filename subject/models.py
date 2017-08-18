# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from books.models import Book
from utils import storage
from utils.const import CHOICE_TOPIC_TYPE


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    type = models.IntegerField(default=0, choices=CHOICE_TOPIC_TYPE, verbose_name=u'类型')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    books = models.ManyToManyField(Book, verbose_name=u'图书')

    class Meta:
        db_table = "t_topic"
        verbose_name = u"专题"
        verbose_name_plural = u"专题"

    def __unicode__(self):
        return self.name


class Column(MPTTModel):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    topics = models.ManyToManyField(Topic, blank=True, related_name='topics')
    books = models.ManyToManyField(Book, blank=True, related_name='column_books')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = "t_column"
        verbose_name = u"栏目"
        verbose_name_plural = u"栏目"

    def __unicode__(self):
        return self.name


class Classification(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'名称')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, storage=storage.ImageStorage())
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

    def icon_img(self):
        if self.icon:
            return '<img src="/media/%s" />' % self.icon
        else:
            return '(no image)'

    icon_img.short_description = 'Thumb'
    icon_img.allow_tags = True


class Ranking(MPTTModel):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    books = models.ManyToManyField(Book, blank=True, related_name='ranking_books')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = "t_ranking"
        verbose_name = u"排行"
        verbose_name_plural = u"排行"

    def __unicode__(self):
        return self.name
