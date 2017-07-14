"""ebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

import index.views as index_views
from banner.views import BannerViewSet
from books.views import BookViewSet
from bookshelf.views import BookshelfViewSet
from classification.views import ClassificationViewSet
from column.views import ColumnViewSet
from hotword.views import HotWordViewSet
from ranking.views import RankingViewSet

router = DefaultRouter()
router.register(r'banner', BannerViewSet)
router.register(r'book', BookViewSet)
router.register(r'bookshelf', BookshelfViewSet)
router.register(r'column', ColumnViewSet)
router.register(r'classification', ClassificationViewSet)
router.register(r'ranking', RankingViewSet)
router.register(r'hotword', HotWordViewSet)

schema_view = get_swagger_view(title='EBook API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/index/bookshelf/$', index_views.api_bookshelf, name='bookshelf'),
    url(r'^api/index/recommendation/$', index_views.api_recommendation, name='recommendation'),
    url(r'^api/index/classification/$', index_views.api_classification, name='classification$'),
    url(r'^api/index/hotword/', index_views.api_keyword, name='hotword'),
    url(r'^api/docs', schema_view),
]

urlpatterns += router.urls
