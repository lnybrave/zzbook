# !/user/bin/python
# -*- coding=utf-8 -*-

import json
import logging
import traceback

from django.http import HttpResponse
from rest_framework.views import APIView

from bookshelf.models import Bookshelf
from classification.models import Classification
from column.models import Column
from ranking.models import Ranking
from hotword.models import HotWord
from utils import err_code

logger = logging.getLogger(__name__)


class ApiBookshelf(APIView):
    pass


def api_bookshelf(request):
    """
    书架
    """
    try:
        books = Bookshelf.objects.all()
        dict_resp = {"c": err_code.ERR_SUCCESS[0], "d": [book.get_format_dict() for book in books]}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")

    except(BaseException,):
        s_err_info = traceback.format_exc()
        logger.error(s_err_info)
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")


def api_recommendation(request):
    """
    精选
    """
    try:
        columns = Column.objects.all()
        dict_resp = {"c": err_code.ERR_SUCCESS[0], "d": [column.get_format_dict() for column in columns]}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")

    except(BaseException,):
        s_err_info = traceback.format_exc()
        logger.error(s_err_info)
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dump(dict_resp, ensure_ascii=False), content_type="application/json")


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
