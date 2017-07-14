#!/usr/bin/python
# coding:utf-8
import json

from django.http import HttpRequest, HttpResponse
from utils import err_code


def check_permission(permission_list):
    """
    拥有权限装饰器
    :param permission_list:  访问接口所需权限集合,拥有其中任意一个权限就可以访问接口，eg: ["add_logentry", "change_logentry"]
    :return:
    """

    def wrapper(func):
        def sub_wrapper(*args, **kwargs):
            has_permission = False
            if not permission_list or not len(permission_list):
                has_permission = True
            else:
                # 遍历所有的参数获取user对象
                for arg in args:
                    # 是否为request
                    if isinstance(arg, HttpRequest):
                        user = arg.user  # 请求用户
                        # 遍历访问接口所需权限集合， 如果有一个权限不满足， 则没有访问权限
                        for permission in permission_list:
                            if user.has_perm(permission):  # 判断有无权限
                                has_permission = True
            if has_permission:  # 拥有权限则放行
                return func(*args, **kwargs)
            else:  # 返回没有权限
                return HttpResponse(json.dumps({"c": err_code.ERR_NO_PERMISSION[0], "m": err_code.ERR_NO_PERMISSION[1]},
                                               ensure_ascii=False), content_type="application/json")

        return sub_wrapper

    return wrapper
