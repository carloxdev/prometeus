# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import Default


urlpatterns = [
    url(r'^$', Default.as_view(), name="default"),
]
