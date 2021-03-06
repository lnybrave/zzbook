# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from menu.models import Menu
from menu.serializers import MenuSerializer
from utils.const import STATUS_ON


class MenuViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    菜单
    """
    queryset = Menu.objects.filter(status=STATUS_ON).all()
    serializer_class = MenuSerializer
    pagination_class = None
