# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin

from menu.models import Menu
from subject.models import Topic, Column, Ranking, Classification


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    菜单
    """
    list_display = ['name', 'desc', 'icon_img', 'is_recommend', 'status']

    exclude = ['del_flag', 'icon_img']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'topic':
            kwargs["queryset"] = Topic.objects.all()
        elif db_field.name == 'column':
            kwargs["queryset"] = Column.objects.filter(level=0)
        elif db_field.name == 'ranking':
            kwargs["queryset"] = Ranking.objects.filter(level=0)
        elif db_field.name == 'classification':
            kwargs["queryset"] = Classification.objects.filter(level=0)
        return super(MenuAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
