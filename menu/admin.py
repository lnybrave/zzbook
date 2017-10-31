# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from suit.admin import SortableModelAdmin

from menu.models import Menu
from subject.models import Topic, Ranking, Classification, Column
from utils import const


@admin.register(Menu)
class MenuAdmin(SortableModelAdmin):
    """
    菜单
    """
    list_display = ['name', 'desc', 'icon_img', 'order', 'status']

    exclude = ['del_flag', 'icon_img']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'topic':
            kwargs["queryset"] = Topic.objects.filter(del_flag=const.DEL_FLAG_NO)
        elif db_field.name == 'column':
            kwargs["queryset"] = Column.objects.all()
        elif db_field.name == 'ranking':
            kwargs["queryset"] = Ranking.objects.filter(level=0, del_flag=const.DEL_FLAG_NO)
        elif db_field.name == 'classification':
            kwargs["queryset"] = Classification.objects.filter(level=0, del_flag=const.DEL_FLAG_NO)
        return super(MenuAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
