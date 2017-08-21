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
from menu.views import MenuViewSet
from recommend.views import RecommendViewSet
from search.views import SearchWordViewSet, SearchBookViewSet, SearchSuggestViewSet, SearchTopViewSet
from subject.views import ClassificationViewSet, RankingItemViewSet, ClassificationBooksViewSet, ColumnViewSet, \
    RankingViewSet, RankingItemBooksViewSet, TopicViewSet, ClassificationItemViewSet

router = DefaultRouter()
router.register(r'api/account/avatar', AvatarViewSet)
router.register(r'api/banner', BannerViewSet)
router.register(r'api/book', BookViewSet)
router.register(r'api/bookshelf', BookshelfViewSet)
router.register(r'api/menu', MenuViewSet)
router.register(r'api/recommend', RecommendViewSet)
router.register(r'api/topic', TopicViewSet)
router.register(r'api/column', ColumnViewSet)
router.register(r'api/classification', ClassificationViewSet)
classification_item = ClassificationItemViewSet.as_view({'get': 'list'})
classification_books = ClassificationBooksViewSet.as_view({'get': 'list'})
router.register(r'api/ranking', RankingViewSet)
ranking_item = RankingItemViewSet.as_view({'get': 'list'})
ranking_item_with_books = RankingItemViewSet.as_view({'get': 'with_books'})
ranking_item_default = RankingItemViewSet.as_view({'get': 'default'})
ranking_item_books = RankingItemBooksViewSet.as_view({'get': 'list'})
router.register(r'api/search', SearchBookViewSet)
router.register(r'api/search/words', SearchWordViewSet)

schema_view = get_swagger_view(title='ZZBook API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/docs', schema_view),
    url(r'^api/classification/(?P<id>\d+)/subitems/$', classification_item),
    url(r'^api/classification/(?P<parent>\d+)/subitems/(?P<id>\d+)/books/$', classification_books),
    url(r'^api/ranking/(?P<id>\d+)/subitems/$', ranking_item),
    url(r'^api/ranking/(?P<id>\d+)/subitems_with_books/$', ranking_item_with_books),
    url(r'^api/ranking/(?P<id>\d+)/books/$', ranking_item_books),
    url(r'^api/search/suggest/$', SearchSuggestViewSet.as_view({'get': 'list'})),
    url(r'^api/search/top/(?P<count>\d+)/$', SearchTopViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
