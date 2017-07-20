# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bookshelf.models import Bookshelf
from bookshelf.serializers import BookshelfSerializer


class BookshelfViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
    pagination_class = None

    @list_route(methods=['get'])
    def recommendation(self, request):
        data_set = self.get_queryset()
        serializer = BookshelfSerializer(data_set, many=True)
        return Response(serializer.data)
