# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import CommentAddAPI


urlpatterns = [
    url(r'^comments/add/$', CommentAddAPI.as_view(), name="comment_add"),
]
