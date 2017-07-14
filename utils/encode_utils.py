#!/usr/bin/python
# coding:utf-8
import base64

from django.http import HttpRequest
from entrepreneurial.settings import DEBUG


def encrypt(en_str):
    """
    加密
    :param en_str: 待加密明文
    :return: 加密后的密文
    """
    return base64.b64encode(en_str)


def decrypt(de_str):
    """
    解密
    :param de_str: 待解密密文
    :return:
    """
    return base64.b64decode(de_str)


def param_descrypt(exclude):
    """
    参数解密装饰器
    :param exclude:  排除字段集合，eg: ["name", "sex"]
    :return:
    """

    if DEBUG:  # 如果是调试模式，直接执行方法
        def wrapper(func):
            return func
    else:
        def wrapper(func):

            def decrypt_param(key, value):
                if key not in exclude:
                    return decrypt(value)
                else:
                    return value

            def decrypt_arg(arg):
                arg.POST = {k: decrypt_param(key=k, value=v) for (k, v) in arg.POST.items()}
                return arg

            def sub_wrapper(*args, **kwargs):
                """
                将参数解密并回填到request中，仅针对POST请求
                """

                [decrypt_arg(arg) for arg in args if isinstance(arg, HttpRequest)]
                return func(*args, **kwargs)

            return sub_wrapper

    return wrapper


if __name__ == '__main__':
    en_str = "admin"
    print en_str
    de_str = encrypt(en_str)
    print de_str
    aaa = decrypt(de_str)
    print aaa
