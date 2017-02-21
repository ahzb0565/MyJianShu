from django.conf.urls import url
from JianShu.apps.main_app.views import *


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]