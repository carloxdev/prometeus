# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import VoucherListPending, BenefitListAdmin, BenefitCancel
from .views import VoucherListAll
from .views import VoucherListAdminPending
from .views import VoucherListAdminAll
from .views import VoucherAdd
from .views import VoucherAddSuccess
from .views import VoucherView
from .views import VoucherEdit
from .views import VoucherCancel

from .views import BenefitList
from .views import BenefitAdd
from .views import BenefitAddSuccess
from .views import BenefitEdit


urlpatterns = [
    url(
        r'^vouchers/pending/$',
        VoucherListPending.as_view(),
        name="voucher_list_pending"
    ),
    url(
        r'^vouchers/all/$',
        VoucherListAll.as_view(),
        name="voucher_list_all"
    ),
    url(
        r'^vouchers/admin/pending/$',
        VoucherListAdminPending.as_view(),
        name="voucher_list_admin_pending"
    ),
    url(
        r'^vouchers/admin/all/$',
        VoucherListAdminAll.as_view(),
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

    url(r'^benefits/pending/$', BenefitList.as_view(), {'status': 'pending'}, name="benefit_list_pending"),
    url(r'^benefits/all/$', BenefitList.as_view(), {'status': 'all'}, name="benefit_list_all"),
    url(r'^benefits/admin/pending/$', BenefitListAdmin.as_view(), {'status': 'pending'}, name="benefit_list_admin_pending"),
    url(r'^benefits/admin/all/$', BenefitListAdmin.as_view(), {'status': 'all'}, name="benefit_list_admin_all"),
    url(r'^benefits/add/$', BenefitAdd.as_view(), name="benefit_add"),
    url(r'^benefits/add/success/$', BenefitAddSuccess.as_view(), name="benefit_add_success"),
    url(r'^benefits/(?P<pk>\d+)/edit/$', BenefitEdit.as_view(), name="benefit_edit"),
    url(r'^benefits/(?P<pk>\d+)/cancel/$', BenefitCancel.as_view(), name="benefit_cancel"),
]
