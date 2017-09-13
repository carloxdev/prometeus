# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import Index


urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
]
