# !/usr/bin/python
# -*- coding=utf-8 -*-
"""
错误码
"""
ERR_SUCCESS = [0, u'成功']
ERR_EXCEPTION = [-1, u'系统异常']
ERR_NO_PERMISSION = [3000, u'没有权限']
ERR_USERNAME_PWD = [4044, u'用户名或密码错误']

ERR_PAGE_OUT_OF_RANGE = [0, u"分页页数过大，没有数据"]
ERR_EXAM_REPEAT = [5003, u"已经考过试了，不可重复考试"]
ERR_TEAM_REPEAT = [5005, u"已经加入过该小组，不需要重复加入"]
ERR_TEAM_NOT_EXIST = [5007, u"还没有加入该小组，无法删除"]
ERR_WORK_REPEAT = [5009, u"已提交过该作业了，不可重复提交"]
ERR_TEAM_USER_NOT_EXIST = [5011, u"还没有加入该小组，无法回答作业"]