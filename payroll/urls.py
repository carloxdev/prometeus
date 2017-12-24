# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import VoucherListView
from .views import VoucherListEdit
from .views import VoucherAdd
from .views import VoucherAddSuccess
from .views import VoucherView
from .views import VoucherEdit
from .views import VoucherCancel

from .views import BenefitListView
from .views import BenefitListEdit
from .views import BenefitCancel
from .views import BenefitAdd
from .views import BenefitAddSuccess
from .views import BenefitEdit


urlpatterns = [

    # Vouchers
    url(
        r'^vouchers/pending/$',
        VoucherListView.as_view(), {'_status': 'pending'},
        name="voucher_list_pending"
    ),
    url(
        r'^vouchers/all/$',
        VoucherListView.as_view(), {'_status': 'all'},
        name="voucher_list_all"
    ),
    url(
        r'^vouchers/admin/pending/$',
        VoucherListEdit.as_view(), {'_status': 'pending'},
        name="voucher_list_admin_pending"
    ),
    url(
        r'^vouchers/admin/all/$',
        VoucherListEdit.as_view(), {'_status': 'all'},
        name="voucher_list_admin_all"
    ),
    url(
        r'^vouchers/add/$',
        VoucherAdd.as_view(),
        name="voucher_add"
    ),
    url(
        r'^vouchers/add/success/$',
        VoucherAddSuccess.as_view(),
        name="voucher_add_success"
    ),
    url(
        r'^vouchers/(?P<pk>\d+)/view/$',
        VoucherView.as_view(),
        name="voucher_view"
    ),
    url(
        r'^vouchers/(?P<pk>\d+)/edit/$',
        VoucherEdit.as_view(),
        name="voucher_edit"
    ),
    url(
        r'^vouchers/(?P<_pk>\d+)/cancel/$',
        VoucherCancel.as_view(),
        name="voucher_cancel"
    ),

    # Benefits
    url(
        r'^benefits/pending/$',
        BenefitListView.as_view(), {'_status': 'pending'},
        name="benefit_list_pending"
    ),
    url(
        r'^benefits/all/$',
        BenefitListView.as_view(), {'_status': 'all'},
        name="benefit_list_all"
    ),
    url(
        r'^benefits/admin/pending/$',
        BenefitListEdit.as_view(), {'_status': 'pending'},
        name="benefit_list_admin_pending"
    ),
    url(
        r'^benefits/admin/all/$',
        BenefitListEdit.as_view(), {'_status': 'all'},
        name="benefit_list_admin_all"
    ),
    url(
        r'^benefits/add/$',
        BenefitAdd.as_view(),
        name="benefit_add"
    ),
    url(
        r'^benefits/add/success/$',
        BenefitAddSuccess.as_view(),
        name="benefit_add_success"
    ),
    url(
        r'^benefits/(?P<pk>\d+)/edit/$',
        BenefitEdit.as_view(),
        name="benefit_edit"
    ),
    url(
        r'^benefits/(?P<pk>\d+)/cancel/$',
        BenefitCancel.as_view(),
        name="benefit_cancel"
    ),
]
