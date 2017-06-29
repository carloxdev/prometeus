# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import NewList
from .views import NewAdd
from .views import NewUpload
from .views import NewAddSuccess
from .views import NewView
from .views import NewEdit


urlpatterns = [
    url(r'^news/$', NewList.as_view(), name="new_list"),
    url(r'^news/add/$', NewAdd.as_view(), name="new_add"),
    url(r'^news/(?P<_pk>\d+)/upload/$', NewUpload.as_view(), name='new_upload'),
    url(r'^news/add/success/$', NewAddSuccess.as_view(), name="new_add_success"),
    url(r'^news/(?P<_pk>\d+)/view/$', NewView.as_view(), name="new_view"),
    url(r'^news/(?P<_pk>\d+)/edit/$', NewEdit.as_view(), name="new_edit"),
]
