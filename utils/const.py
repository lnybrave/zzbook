#!/usr/bin/python
# coding:utf-8

# 实验root菜单
lab_menu_parent = 7

# 小组root菜单
team_menu_parent = 4

# 作业root菜单
work_menu_parent = 5

# 文件上传接口文件保存路径
API_FILE_SAVE_PATH = 'api'

# 用户类型
USER_TYPE_STUDENT = '1'
USER_TYPE_TEACHER = '2'
CHOICE_USER_TYPE = (
    (USER_TYPE_STUDENT, u"学生"),
    (USER_TYPE_TEACHER, u"老师")
)

# 性别
MALE = '1'
FEMALE = '2'
CHOICE_GENDER = (
    (MALE, u"男"),
    (FEMALE, u"女")
)

# 是否
GLOBAL_YES = '1'
GLOBAL_NO = '0'
CHOICE_YES_NO = (
    (GLOBAL_YES, u"是"),
    (GLOBAL_NO, u"否")
)

# 删除标记
DEL_FLAG_YES = 1
DEL_FLAG_NO = 0
CHOICE_DELETE = (
    (DEL_FLAG_YES, u"是"),
    (DEL_FLAG_NO, u"否")
)

# 频道类型
SUBJECT_COLUMN = 1
SUBJECT_RANKING = 2
SUBJECT_CLASSIFICATION = 3
SUBJECT_SEARCH = 4
CHOICE_SUBJECT_TYPE = (
    (SUBJECT_COLUMN, u"栏目"),
    (SUBJECT_RANKING, u"排行"),
    (SUBJECT_CLASSIFICATION, u"分类"),
    (SUBJECT_SEARCH, u"搜索"),
)

# 频道唯一码
SUBJECT_CODE_RECOMMENDATION = "subject_recommendation"

# 专题类型
CHOICE_TOPIC_TYPE = (
    (1, u"广告"),
    (2, u"书名+封面"),
    (3, u"书名+封面+简介"),
)
