#!/usr/bin/python
# -*- coding: utf-8 -*-
import types


# time对象转字符串，返回""或2015-12-12 10:10:10
def time2str(time):
    if time == None:
        return ""

    sTime = str(time)
    sTime = sTime.strip()
    if len(sTime) >= 19:
        sTime = sTime[:19]

    return sTime


# 返回url对象
def url2str(obj):
    try:
        return obj.url
    except:
        return ""


# 空对象转字符串
def null2str(data, default=""):
    if isinstance(data, types.NoneType):
        return default
    elif isinstance(data, types.IntType) or isinstance(data, types.FloatType):
        return str(data)
    else:
        return data


# 空对象转数字
def null2int(data, default=0):
    if isinstance(data, types.NoneType):
        return default
    else:
        return int(data)


# 判断对象是否为空，如是不为空，返回对象字符串
def obj2str(obj, field):
    if not obj:
        return ""
    else:
        val = getattr(obj, field)
        return null2str(val)
