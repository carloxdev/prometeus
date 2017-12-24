# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views_rest import VoucherTypeAPIView


urlpatterns = [
    url(
        r'^vouchertype/(?P<pk>\d+)/$',
        VoucherTypeAPIView.as_view(),
        name="vouchertype-retrieve"
    ),
]
