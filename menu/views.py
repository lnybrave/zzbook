# !/bin/user/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from menu.models import Menu
from menu.serializers import MenuSerializer


class MenuViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = None
