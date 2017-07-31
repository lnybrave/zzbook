# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from books.models import Book
from subject.models import Topic
from utils import storage
from utils.const import CHOICE_BANNER


class Banner(models.Model):
    """
    广告，注意广告不要使用ad等类似单词，会被屏蔽广告插件屏蔽
    """
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    img = models.ImageField(upload_to='banners/', storage=storage.ImageStorage(), verbose_name=u'图片')
    type = models.IntegerField(default=0, choices=CHOICE_BANNER, verbose_name=u'类型')
    sort = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    book = models.ForeignKey(Book, blank=True, null=True, related_name='book')
    topic = models.ForeignKey(Topic, blank=True, null=True, related_name='topic')

    class Meta:
        db_table = "t_banner"
        verbose_name = u"广告"
        verbose_name_plural = u"广告"

    def __unicode__(self):
        return self.name

    def banner_img(self):
        if self.img:
            return '<img src="/media/%s" />' % self.img
        else:
            return '(no image)'

    banner_img.short_description = 'Thumb'
    banner_img.allow_tags = True
