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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from account.views import AvatarViewSet
from banner.views import BannerViewSet
from books.views import BookViewSet
from bookshelf.views import BookshelfViewSet
from search.views import SearchWordViewSet, SearchBookViewSet, SearchSuggestViewSet, SearchTopViewSet
from subject.views import ColumnTopicViewSet, ClassificationViewSet, RankingViewSet, SubjectViewSet, ColumnViewSet, \
    ClassificationBooksViewSet

router = DefaultRouter()
router.register(r'api/account/avatar', AvatarViewSet)
router.register(r'api/banner', BannerViewSet)
router.register(r'api/book', BookViewSet)
router.register(r'api/bookshelf', BookshelfViewSet)
router.register(r'api/subject', SubjectViewSet)
router.register(r'api/column', ColumnViewSet)
router.register(r'api/column/topic', ColumnTopicViewSet)
router.register(r'api/classification', ClassificationViewSet)
router.register(r'api/ranking', RankingViewSet)
router.register(r'api/search', SearchBookViewSet)
router.register(r'api/search/words', SearchWordViewSet)

schema_view = get_swagger_view(title='ZZBook API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/docs', schema_view),
    url(r'^api/classification/(?P<first_id>\d+)/(?P<second_id>\d+)/books/$',
        ClassificationBooksViewSet.as_view({'get': 'books'})),
    url(r'^api/search/suggest/$', SearchSuggestViewSet.as_view({'get': 'list'})),
    url(r'^api/search/top/(?P<count>\d+)?', SearchTopViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
