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
    # 完结了的图书不更新信息
    if Book.objects.filter(id=bid, status=1).count() == 0:
        page = urllib2.urlopen("http://wap.cmread.com/r/p/viewdata.jsp?bid=%s&cm=%s&vt=9" % (bid, cm))
        data = page.read()

        try:
            result = json.loads(data, encoding="utf-8")
            print result

            update = Book.objects.filter(id=bid).count() != 0

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
            if update:
                book.save(force_update=update, update_fields=(
                    'name', 'brief', 'desc', 'cover_url', 'cover_url_small', 'status', 'first_cid', 'last_cid',
                    'chapter_size', 'score', 'word_size', 'click_amount', 'kw', 'price', 'charge_mode'))
            else:
                book.save(force_insert=True)
                return True

        except Exception, e:
            print e.message
    return False


# 同步书架
def sync_bookshelf():
    url = "%s/smart_book/get_bookshelf" % domain
    page = urllib2.urlopen(url)
    result = json.loads(page.read())
    print result
    books = result['bookshelf']

    update_count = 0
    for index, b in enumerate(books):
        if sync_book(b['book_id'], 'zm'):
            update_count += 1
    return len(books), update_count


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    """
    数据
    """

    list_display = ['name']

    actions = ['sync_data']

    def sync_data(self, request, queryset):
        total, update = sync_bookshelf()
        message = "总共%d本，同步了%d本" % (total, update)
        print message
        self.message_user(request, message)

    sync_data.short_description = "同步所选的 数据"

admin.site.disable_action('delete_selected')
