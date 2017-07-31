# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from books.models import Book
from utils import storage
from utils.const import CHOICE_SUBJECT_TYPE, CHOICE_TOPIC_TYPE


class Subject(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    code = models.CharField(max_length=64, unique=True, verbose_name=u'唯一码')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    is_recommend = models.BooleanField(default=False, verbose_name=u'精选')
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, storage=storage.ImageStorage(),
                             verbose_name=u'自定义图标')
    type = models.IntegerField(default=0, choices=CHOICE_SUBJECT_TYPE, verbose_name=u'类型')

    class Meta:
        db_table = "t_subject"
        verbose_name = u"频道"
        verbose_name_plural = u"频道"
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


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    type = models.IntegerField(default=0, choices=CHOICE_TOPIC_TYPE, verbose_name=u'类型')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, verbose_name=u'删除')
    subject = models.ForeignKey(Subject, verbose_name=u'所属频道')
    books = models.ManyToManyField(Book, verbose_name=u'图书')

    class Meta:
        db_table = "t_topic"
        verbose_name = u"专题"
        verbose_name_plural = u"专题"

    def __unicode__(self):
        return self.name


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
