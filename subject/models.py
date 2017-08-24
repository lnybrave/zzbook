# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from books.models import Book
from utils import storage
from utils.const import CHOICE_TOPIC_TYPE, CHOICE_STATUS


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    type = models.IntegerField(default=0, choices=CHOICE_TOPIC_TYPE, verbose_name=u'类型')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')

    class Meta:
        db_table = "t_topic"
        verbose_name = u"专题"
        verbose_name_plural = u"专题"

    def __unicode__(self):
        return self.name


class TopicConfig(models.Model):
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    item = models.ForeignKey(Topic, verbose_name=u'专题')
    book = models.ForeignKey(Book, blank=True, null=True, verbose_name='图书')

    class Meta:
        db_table = "t_topic_config"
        verbose_name = u"专题配置"
        verbose_name_plural = u"专题配置"

    def item_name(self):
        if self.item is not None:
            return self.item.name
        return "no title"

    item_name.short_description = '名称'
    item_name.allow_tags = True

    def title(self):
        if self.book is not None:
            return self.book.name
        return "no title"

    title.short_description = '名称'
    title.allow_tags = True

    def type(self):
        if self.book is not None:
            return "图书"
        return "unknown"


class Column(MPTTModel):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    order = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = "t_column"
        verbose_name = u"栏目"
        verbose_name_plural = u"栏目"
        ordering = ('order',)

    def __unicode__(self):
        return self.name


class ColumnConfig(models.Model):
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    item = models.ForeignKey(Column, verbose_name=u'栏目')
    topic = models.ForeignKey(Topic, blank=True, null=True, verbose_name='专题')
    book = models.ForeignKey(Book, blank=True, null=True, verbose_name='图书')

    class Meta:
        db_table = "t_column_config"
        verbose_name = u"栏目配置"
        verbose_name_plural = u"栏目配置"

    def item_name(self):
        if self.item is not None:
            return self.item.name
        return "no title"

    item_name.short_description = '名称'
    item_name.allow_tags = True

    def title(self):
        if self.topic is not None:
            return self.topic.name
        if self.book is not None:
            return self.book.name
        return "no title"

    title.short_description = '名称'
    title.allow_tags = True

    def type(self):
        if self.topic is not None:
            return "专题"
        if self.book is not None:
            return "图书"
        return "unknown"


class Classification(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'名称')
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, storage=storage.ImageStorage())
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
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


class ClassificationConfig(models.Model):
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    item = models.ForeignKey(Classification, verbose_name=u'分类')
    book = models.ForeignKey(Book, blank=True, null=True, verbose_name='图书')

    class Meta:
        db_table = "t_classification_config"
        verbose_name = u"分类配置"
        verbose_name_plural = u"分类配置"

    def item_name(self):
        if self.item is not None:
            return self.item.name
        return "no title"

    item_name.short_description = '名称'
    item_name.allow_tags = True

    def title(self):
        if self.book is not None:
            return self.book.name
        return "no title"

    title.short_description = '名称'
    title.allow_tags = True

    def type(self):
        if self.book is not None:
            return "图书"
        return "unknown"


class Ranking(MPTTModel):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = "t_ranking"
        verbose_name = u"排行"
        verbose_name_plural = u"排行"

    def __unicode__(self):
        return self.name


class RankingConfig(models.Model):
    order = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=CHOICE_STATUS, verbose_name=u'状态')
    item = models.ForeignKey(Ranking, verbose_name=u'排行')
    book = models.ForeignKey(Book, blank=True, null=True, verbose_name='图书')

    class Meta:
        db_table = "t_ranking_config"
        verbose_name = u"排行配置"
        verbose_name_plural = u"排行配置"

    def item_name(self):
        if self.item is not None:
            return self.item.name
        return "no title"

    item_name.short_description = '名称'
    item_name.allow_tags = True

    def title(self):
        if self.book is not None:
            return self.book.name
        return "no title"

    title.short_description = '名称'
    title.allow_tags = True

    def type(self):
        if self.book is not None:
            return "图书"
        return "unknown"
