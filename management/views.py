# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View

# Own's Libraries
from payroll.business import VoucherRequisitionBusiness
from payroll.business import BenefitRequisitionBusiness
from labor.business import IncidentReportBusiness


class TaskList(View):
    template_name = "task_list.html"

    def get(self, _request):
        new_vouchers = VoucherRequisitionBusiness.get_No_Pendings()
        new_benefits = BenefitRequisitionBusiness.get_No_Pendings()
        new_incidents = IncidentReportBusiness.get_No_Pendings()

        context = {
            'new_vouchers': new_vouchers,
            'new_benefits': new_benefits,
            'new_incidents': new_incidents,
        }
        return render(_request, self.template_name, context)
