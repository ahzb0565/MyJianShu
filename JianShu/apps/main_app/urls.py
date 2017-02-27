from django.conf.urls import url
from JianShu.apps.main_app.views import *


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]