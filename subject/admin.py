# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import TreeRelatedFieldListFilter

from subject.models import Subject, Topic, Ranking, Classification
from utils.const import SUBJECT_COLUMN


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    频道
    """

    list_display = ['name', 'desc', 'code', 'icon_img', 'is_recommend', 'status']
    readonly_fields = ('icon_img',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    专题
    """

    list_display = ['name', 'desc', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subject':
            kwargs["queryset"] = Subject.objects.filter(type=SUBJECT_COLUMN)
        return super(TopicAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    model = Ranking
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    model = Classification
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']

    exclude = ['del_flag']

    filter_horizontal = ['books']
