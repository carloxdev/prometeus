# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import View
from django.urls import reverse_lazy

# Own's Libraries
from security.mixins import GroupLoginRequiredMixin
from .business import VoucherRequisitionBusiness as VoucherBusiness

from .models import VoucherRequisition
from .forms import VoucherRequisitionAddForm


class VoucherList(GroupLoginRequiredMixin, View):
    template_name = "voucher/list.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_FilterBy(
            query,
            _request.user.profile
        )
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherAdd(GroupLoginRequiredMixin, CreateView):
    template_name = "voucher/add.html"
    model = VoucherRequisition
    form_class = VoucherRequisitionAddForm
    success_url = reverse_lazy('payroll:voucher_list')

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user.profile
    #     return super(VoucherAdd, self).form_valid(form)


class VoucherAddSuccess(View):
    template_name = "voucher_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class VoucherView(View):
    template_name = "voucher_view.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class VoucherEdit(View):
    template_name = "voucher_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class BenefitList(View):
    template_name = "benefit_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitAdd(View):
    template_name = "benefit_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitAddSuccess(View):
    template_name = "benefit_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitView(View):
    template_name = "benefit_view.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class BenefitEdit(View):
    template_name = "benefit_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
