# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View

# Own's Libraries
from payroll.business import VoucherRequisitionBusiness


class EmailConfig(View):
    template_name = "email.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class TaskList(View):
    template_name = "task_list.html"

    def get(self, _request):
        new_vouchers = VoucherRequisitionBusiness.get_No_Pending()

        context = {
            'new_vouchers': new_vouchers
        }
        return render(_request, self.template_name, context)


class TaskBenefits(View):
    template_name = "task_benefits.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class TaskIncidences(View):
    template_name = "task_incidences.html"

    def get(self, _request):
        return render(_request, self.template_name, {})
