# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.db import models

from account.models import User
from utils import storage
from utils.const import CHOICE_BOOK_STATUS, CHOICE_CHARGE_MODE


class Book(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=u'ID')
    name = models.CharField(max_length=128, verbose_name=u'名称')
    brief = models.CharField(max_length=256, verbose_name=u'简介')
    desc = models.CharField(max_length=512, blank=True, null=True, verbose_name=u'描述')
    cover = models.ImageField(upload_to='images/', blank=True, null=True, storage=storage.ImageStorage(),
                              verbose_name=u'自定义图片')
    cover_url = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'大图url')
    cover_url_small = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'小图url')
    status = models.IntegerField(default=0, choices=CHOICE_BOOK_STATUS, verbose_name=u'状态')
    first_cid = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'第一章id')
    last_cid = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'倒数第一章id')
    chapter_size = models.IntegerField(default=0, verbose_name=u'章节数')
    score = models.FloatField(default=0, verbose_name=u'分数')
    word_size = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'字数')
    click_amount = models.IntegerField(default=0, verbose_name=u'点击量')
    kw = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'关键字')
    price = models.IntegerField(default=0, verbose_name=u'价格(分)')
    charge_mode = models.IntegerField(default=0, choices=CHOICE_CHARGE_MODE, verbose_name=u'付费模式')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    author = models.ManyToManyField(User, blank=True, verbose_name=u'作者')

    class Meta:
        db_table = "t_book"
        verbose_name = u"图书"
        verbose_name_plural = u"图书"

    def __unicode__(self):
        return self.name

    def author_names(self):
        return [author.name for author in self.author.filter(book=self)]

    author_names.short_description = u"作者"

    def cover_img(self):
        if self.cover:
            return '<img src="/media/%s" />' % self.cover
        elif self.cover_url:
            return '<img src="%s" />' % self.cover_url
        elif self.cover_url_small:
            return '<img src="%s" />' % self.cover_url_small
        else:
            return '(no image)'

    cover_img.short_description = '封面'
    cover_img.allow_tags = True


class Content(models.Model):
    book = models.ForeignKey(Book)
    prev_cid = models.IntegerField(default=0, verbose_name=u"上一章id")
    next_cid = models.IntegerField(default=0, verbose_name=u"下一章id")

    class Meta:
        db_table = "t_content"
        verbose_name = u"目录"
        verbose_name_plural = u"目录"
