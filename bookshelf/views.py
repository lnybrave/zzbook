# !/usr/bin/python
# -*- coding=utf-8 -*-

from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from banner.models import Banner
from banner.serializers import BannerSerializer
from books.models import Book
from books.serializers import BookSerializer


class BookshelfViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Book.objects.filter(bookshelf__isnull=False).order_by('-bookshelf__sort')
    serializer_class = BookSerializer
    pagination_class = None

    @list_route(methods=['get'])
    def banner(self, request):
        """
        书架广告
        """
        qs = Banner.objects.filter(type=2).all()
        serializer = BannerSerializer(qs, many=True)
        return Response(serializer.data)
