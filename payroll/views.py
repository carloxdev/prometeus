# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View


class VoucherList(View):
    template_name = "voucher_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class VoucherAdd(View):
    template_name = "voucher_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


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
