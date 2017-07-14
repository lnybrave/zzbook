# coding=utf-8
import MySQLdb
from django.db.models import ManyToManyRel, ManyToOneRel, ForeignKey

from entrepreneurial import settings
from django.apps import apps
import os, django


# Create your tests here.

def get_db_connection():
    """
    获取数据库连接
    :return: 
    """
    conn = MySQLdb.connect(
        host=settings.HOST,
        port=3306,
        user=settings.DB_USER,
        passwd=settings.DB_PWD,
        db=settings.DB_NAME,
        charset="utf8"
    )
    return conn


def get_model_field(app_name):
    """
    处理一个app下所有model关联的表    
    :param app_name: 
    :return: 
    """
    if app_name.__contains__('.'):
        names = app_name.split(".")
        app_name = names[names.__len__() - 1]
    # 获取一个app
    app = apps.get_app_config(app_name)
    # 获取app下的所有model
    models = app.get_models()
    connect = get_db_connection()
    cur = connect.cursor()

    for item in models:
        # print item
        table_name = str(item._meta.db_table)
        table_remark = str(item._meta.verbose_name)
        print "表名称==" + table_name
        print "表注释==" + table_remark
        sql = "alter table " + table_name + " comment '" + table_remark + "';"
        print sql
        # 修改表的备注
        cur.execute(sql)
        cur.close()
        connect.commit()

        # 查询出表的DDL：
        cur = connect.cursor()
        cur.execute("show create table " + table_name + ";")
        datas = cur.fetchall()
        # 表的构造sql
        table_create_sql = datas[0][1]
        left = table_create_sql.find('(') + 1
        right = table_create_sql.rfind(')') - 1
        lines = table_create_sql[left:right].split('\n')
        fileds = item._meta.get_fields()
        lines = lines[0:len(fileds)+1]
        # print "截取结果=" + str(lines)
        for field in fileds:
            # 多对多类型和多对一类型没有对应model，无法读取verbose_name进行同步注释
            if not (isinstance(field, ManyToManyRel) or isinstance(field, ManyToOneRel)):
                # print field.verbose_name
                # print field.name
                col_name = str(field.name)
                col_remark = str(field.verbose_name)
                if isinstance(field, ForeignKey):
                    col_name = col_name + "_id"
                for line in lines:
                    line = str.lstrip(str(line))
                    if line.endswith(','):
                        line = str.rstrip(line, ',')
                    if "`" + col_name + "`" in line and line.startswith("`" + col_name + "`"):
                        sql = "alter table " + table_name + " modify column " + line + " comment '" + col_remark + "';"
                        print sql
                        cur.execute(sql)

    # 关闭数据库连接
    cur.close()
    connect.commit()
    connect.close()


def get_models():
    """
    读取应用设置中所有app下的model
    :return: 
    """
    for item in settings.INSTALLED_APPS:
        get_model_field(item)


if __name__ == '__main__':
    # 加载当前项目的环境
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entrepreneurial.settings")
    django.setup()
    get_models()
