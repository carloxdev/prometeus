# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import LandingView


urlpatterns = [
    url(r'^$', LandingView.as_view(), name="landing"),
]
