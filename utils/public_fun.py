#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import time

# 构造文件名称
from django.core.mail import send_mail

from ebook.settings import EMAIL_FROM


def makename(name):
    # 文件扩展名
    ext = os.path.splitext(name)[1]

    # 定义文件名，年月日时分秒随机数
    fn = time.strftime('%Y%m%d%H%M%S')
    fn += '_%d' % random.randint(1, 10000)
    # 重写合成文件名
    name = fn + ext
    return name


# 随机生成验证码
def randomCode(length):
    num = '0123456789'
    return ''.join(random.sample(num, length))


# 发送邮箱验证码
def send_email_code(email, code, type=1):
    if type == 1:
        email_title = "注册"
        email_body = "验证码：{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
        return True
    else:
        return False
