# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('editorial.urls', namespace="editorial")),
    url(r'', include('home.urls', namespace="home")),
    url(r'', include('labor.urls', namespace="labor")),
    url(r'', include('management.urls', namespace="management")),
    url(r'', include('payroll.urls', namespace="payroll")),
    url(r'', include('security.urls', namespace="security")),
]
