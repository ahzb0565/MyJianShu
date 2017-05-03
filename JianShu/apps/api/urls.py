from django.conf.urls import url

from JianShu.apps.api.apis import *


urlpatterns = [
    url(r'^articles/$', ArticleView.as_view(), name='articles'),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name='article-details'),
]