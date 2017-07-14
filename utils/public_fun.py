#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import random

# 构造文件名称
def makename(name):
    #文件扩展名
    ext = os.path.splitext(name)[1]

    #定义文件名，年月日时分秒随机数
    fn = time.strftime('%Y%m%d%H%M%S')
    fn += '_%d' % random.randint(1, 10000)
    #重写合成文件名
    name = fn + ext
    return name

# 随机生成验证码
def randomCode(length):
    num = '0123456789'
    return ''.join(random.sample(num, length))