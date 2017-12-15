# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import VoucherList
from .views import VoucherListAll
from .views import VoucherListAdmin
from .views import VoucherListAdminAll
from .views import VoucherAdd
from .views import VoucherAddSuccess
from .views import VoucherView
from .views import VoucherEdit
from .views import VoucherCancel

from .views import BenefitList
from .views import BenefitAdd
from .views import BenefitAddSuccess
from .views import BenefitView
from .views import BenefitEdit


urlpatterns = [
    url(r'^vouchers/$', VoucherList.as_view(), name="voucher_list"),
    url(r'^vouchers_all/$', VoucherListAll.as_view(), name="voucher_list_all"),
    url(
        r'^vouchers_admin/$',
        VoucherListAdmin.as_view(),
        name="voucher_list_admin"
    ),
    url(
        r'^vouchers_admin_all/$',
        VoucherListAdminAll.as_view(),
        name="voucher_list_admin_all"
    ),
    url(r'^vouchers/add/$', VoucherAdd.as_view(), name="voucher_add"),
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

    url(r'^benefits/$', BenefitList.as_view(), name="benefit_list"),
    url(r'^benefits/add/$', BenefitAdd.as_view(), name="benefit_add"),
    url(r'^benefits/add/success/$', BenefitAddSuccess.as_view(), name="benefit_add_success"),
    url(r'^benefits/(?P<pk>\d+)/view/$', BenefitView.as_view(), name="benefit_view"),
    url(r'^benefits/(?P<_pk>\d+)/edit/$', BenefitEdit.as_view(), name="benefit_edit"),
]
