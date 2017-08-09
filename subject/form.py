# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.forms import ModelForm

from subject.models import Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
