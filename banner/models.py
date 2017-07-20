# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models

from books.models import Book
from column.models import Topic
from utils import storage


class Banner(models.Model):
    """
    广告，注意广告不要使用ad等类似单词，会被屏蔽广告插件屏蔽
    """
    name = models.CharField(max_length=128, verbose_name=u'名称')
    desc = models.CharField(max_length=256, verbose_name=u'描述')
    img = models.ImageField(upload_to='images/', storage=storage.ImageStorage(), verbose_name=u'图片')
    type = models.IntegerField(default=0, verbose_name=u'类型')
    status = models.IntegerField(default=1, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    book = models.ForeignKey(Book, blank=True)
    topic = models.ForeignKey(Topic, blank=True)

    class Meta:
        db_table = "t_banner"
        verbose_name = u"广告表"
        verbose_name_plural = u"广告表"

    def __unicode__(self):
        return self.name

    def get_format_dict(self):
        return {
            "id": self.pk,
            "name": self.name,
            "desc": self.desc,
            "img": self.img,
            "type": self.type
        }
