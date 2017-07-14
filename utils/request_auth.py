#!/usr/bin/python
# -*- coding: utf-8 -*-


#是否检查登录
IS_CHECK_LOGIN = True

#用户类型
CON_LOGIN_TYPE_USER = 1 #用户
CON_LOGIN_TYPE_STAFF = 3 #员工

CON_KEY = u'_!@#'
ERR_SUCCESS = [0, u'完成']
ERR_USER_NOTLOGGED = [40004, u'用户未登录']
ERR_USER_AUTH = [40005, u'用户权限不够']
ERR_REQUESTWAY = [40006, u'请求方式错误']


def auth_check(request, sMethod="POST", lstModule=None, bChcekLogin=True):
    dictResp = {}
    if not IS_CHECK_LOGIN:
        return dictResp

    if bChcekLogin:
        if not request.user.is_authenticated():
            dictResp = {'c': ERR_USER_NOTLOGGED[0], 'm': ERR_USER_NOTLOGGED[1]}
            return dictResp

    #if request.user.username == 'admin':
    #    return dictResp

    # if lstModule:
    #     for iModule in lstModule:
    #         if "%s," % iModule in request.user.first_name:
    #             #dictResp = {'c': CON_CODE_USER_AUTH_ERR}
    #             return dictResp
    #     else:
    #         dictResp = {'c': ERR_USER_AUTH[0], 'm':ERR_USER_AUTH[1]}
    #
    if request.method != sMethod.upper():
         dictResp = {'c': ERR_REQUESTWAY[0], 'm': ERR_REQUESTWAY[1]}

    return dictResp


def makeLoginName(sKey, Phone):
   return "%s%s%s" % (sKey, CON_KEY, Phone)

def analyLoginName(username):
    return username.split(CON_KEY)[1]





