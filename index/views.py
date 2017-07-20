# !/user/bin/python
# -*- coding=utf-8 -*-

import json
import logging
import traceback

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from banner.models import Banner
from banner.serializers import BannerSerializer
from books.models import Book
from books.serializers import BookSerializer
from classification.models import Classification
from column.models import Column, Subject
from column.serializers import ColumnSerializer
from hotword.models import HotWord
from ranking.models import Ranking
from subject.serializers import SubjectSerializer
from utils import err_code

logger = logging.getLogger(__name__)


@api_view(['GET'])
def api_bookshelf(request):
    """
    书架
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IndexBookshelf(APIView):
    """
    书架
    """

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def api_recommendation(request):
    """
    精选
    """
    banners = Banner.objects.all()
    banner_serializer = BannerSerializer(banners, many=True)

    subjects = Subject.objects.all()
    subject_serializer = SubjectSerializer(subjects, many=True)

    columns = Column.objects.all()
    column_serializer = ColumnSerializer(columns, many=True)

    data = {
        'banners': banner_serializer.data,
        'subjects': subject_serializer.data,
        'columns': column_serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view()
def api_ranking(request):
    """
    排行
    """
    try:
        rankings = Ranking.objects.all()
        dict_resp = {"c": err_code.ERR_SUCCESS[0], "d": [ranking.get_format_dict() for ranking in rankings]}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")

    except(BaseException,):
        s_err_info = traceback.format_exc()
        logger.error(s_err_info)
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dump(dict_resp, ensure_ascii=False), content_type="application/json")


@api_view()
def api_classification(request):
    """
    分类
    """
    try:
        classifications = Classification.objects.all()
        dict_resp = {"c": err_code.ERR_SUCCESS[0],
                     "d": [classification.get_format_dict() for classification in classifications]}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")

    except(BaseException,):
        s_err_info = traceback.format_exc()
        logger.error(s_err_info)
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dump(dict_resp, ensure_ascii=False), content_type="application/json")


@api_view()
def api_keyword(request):
    """
    搜索关键词
    """
    try:
        keywords = HotWord.objects.all()
        dict_resp = {"c": err_code.ERR_SUCCESS[0], "d": [keyword.get_format_dict() for keyword in keywords]}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")

    except(BaseException,):
        s_err_info = traceback.format_exc()
        logger.error(s_err_info)
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dump(dict_resp, ensure_ascii=False), content_type="application/json")
