# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import PostList
from .views import PostAdd
from .views import PostEdit
from .views import PostView


urlpatterns = [
    url(r'^post/$', PostList.as_view(), name="post_list"),
    url(r'^post/add/$', PostAdd.as_view(), name="post_add"),
    url(r'^post/(?P<_pk>\d+)/edit/$', PostEdit.as_view(), name="post_edit"),
    url(r'^post/(?P<_pk>\d+)/view/$', PostView.as_view(), name="post_view"),
]
