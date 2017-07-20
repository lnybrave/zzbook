# !/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from mptt.admin import TreeRelatedFieldListFilter

from classification.models import Classification


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    model = Classification
    list_filter = (
        ('children', TreeRelatedFieldListFilter),
    )

    list_display = ['name', 'status', 'sort']
