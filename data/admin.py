# !/usr/bin/python
# -*- coding=utf-8 -*-
import json
import urllib2

from django.contrib import admin

from books.models import Book
from data.models import Data

domain = "http://smartebook.zmapp.com:9026"


# 同步图书详情
def sync_book(bid, cm):
    page = urllib2.urlopen("http://wap.cmread.com/r/p/viewdata.jsp?bid=%s&cm=%s&vt=9" % (bid, cm))
    data = page.read()
    print data

    try:
        result = json.loads(data, encoding="utf-8")

        book = Book()
        book.pk = int(bid)
        book.name = result['showName']
        book.brief = result['brief']
        book.desc = result['desc']
        book.cover_url = result['bigCoverLogo']
        book.cover_url_small = result['smallCoverLogo']
        book.status = result['status']
        book.first_cid = result['firstChpaterCid']
        book.last_cid = result['lastChapterCid']
        book.chapter_size = result['chapterSize']
        book.score = result['score']
        book.word_size = result['wordSize']
        book.click_amount = result['clickValue']
        book.kw = result['kw']
        book.price = int(float(result['price']) * 100)
        book.charge_mode = result['chargeMode']
        book.save(force_update=True, update_fields=(
            'name', 'brief', 'desc', 'cover_url', 'cover_url_small', 'status', 'first_cid', 'last_cid', 'chapter_size',
            'score', 'word_size', 'click_amount', 'kw', 'price', 'charge_mode'))
    except Exception, e:
        print e.message


# 同步书架
def sync_bookshelf():
    url = "%s/smart_book/get_bookshelf" % domain
    page = urllib2.urlopen(url)
    result = json.loads(page.read())
    for index, b in enumerate(result['bookshelf']):
        sync_book(b['book_id'], 'zm')


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    """
    数据
    """

    list_display = ['name']

    actions = ['sync_data']

    def sync_data(self, request, queryset):
        print 'sync data success'
        sync_bookshelf()
        self.message_user(request, "successfully marked as published.")

    sync_data.short_description = "Mark selected stories as published"
