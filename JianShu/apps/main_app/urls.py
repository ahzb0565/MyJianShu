from django.conf.urls import url
from JianShu.apps.main_app.views import *
from .apis import *


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]

urlpatterns += [
    url(r'^api/articles/$', ArticleView.as_view(), name='articles'),
    url(r'^api/article/(?P<pk>\d+)/$', ArticleView.as_view(), name='article'),
]