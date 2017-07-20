# !/user/bin/python
# -*- coding=utf-8 -*-
import json
import sqlite3
import urllib2

domain = "http://smartebook.zmapp.com:9026"

conn = sqlite3.connect("db.sqlite3", timeout=20)


# 同步图书详情
def sync_book(bid, cm):
    page = urllib2.urlopen("http://wap.cmread.com/r/p/viewdata.jsp?bid=%s&cm=%s&vt=9" % (bid, cm))
    data = page.read()
    print data

    try:
        result = json.loads(data, encoding="utf-8")
        sql = 'INSERT INTO t_book VALUES(%d, \'%s\',\'%s\')' % (int(bid), result['showName'], result['brief'])
        conn.execute(sql)
        conn.commit()
    except Exception, e:
        print e.message


# 同步书架
def sync_bookshelf():
    url = "%s/smart_book/get_bookshelf" % domain
    page = urllib2.urlopen(url)
    result = json.loads(page.read())
    for index, b in enumerate(result['bookshelf']):
        bid = int(b['book_id'])

        try:
            sql = 'INSERT INTO t_bookshelf(book_id, sort, create_time, update_time)' \
                  ' VALUES(%d, %d, datetime(\'now\',\'localtime\'), datetime(\'now\',\'localtime\'))' % (bid, index)
            conn.execute(sql)
            conn.commit()
        except Exception, e:
            print e.message

        sync_book(bid, 'zm')


# 同步排行详情
def sync_ranking_detail(class_id):
    url = "%s/smart_book/get_rank_detail" % domain
    req = urllib2.Request(url, data=json.dumps({"class_id": class_id}))
    page = urllib2.urlopen(req)
    result = json.loads(page.read())
    for b in result['books']:
        sync_book(b['book_id'], 'zm')


# 同步排行
def sync_ranking():
    page = urllib2.urlopen("%s/smart_book/get_rank_class" % domain)
    result = json.loads(page.read())
    for c in result['rank_subjects']:
        # TODO 一级排行
        for d in c['classes']:
            # TODO 二级排行
            sync_ranking_detail(d['class_id'])


# 同步分类详情
def sync_classification_detail(class_id):
    url = "%s/smart_book/get_class_detail" % domain
    req = urllib2.Request(url, data=json.dumps({"class_id": class_id, "offset": 0, "count": 2000}))
    page = urllib2.urlopen(req)
    result = json.loads(page.read())
    for b in result['books']:
        sync_book(b['book_id'], 'zm')


# 同步分类
def sync_classification():
    page = urllib2.urlopen("%s/smart_book/get_class" % domain)
    result = json.loads(page.read())
    for c in result['class_subjects']:
        # TODO 一级分类
        for d in c['columns']:
            # TODO 二级分类
            for e in d['classes']:
                # TODO 三级分类
                sync_classification_detail(e['class_id'])


sync_bookshelf()

# sync_ranking()

# sync_classification()

conn.close()
