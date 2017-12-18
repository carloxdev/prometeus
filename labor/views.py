# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import View


# Own's Libraries
from security.mixins import GroupLoginRequiredMixin

from .models import IncidenceDocument


class IncidentListPending(GroupLoginRequiredMixin, View):
    template_name = "incident_list.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAll(GroupLoginRequiredMixin, View):
    template_name = "incident_list.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAdminPending(GroupLoginRequiredMixin, View):
    template_name = "incident_list.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAdminAll(GroupLoginRequiredMixin, View):
    template_name = "incident_list.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAdd(GroupLoginRequiredMixin, View):
    template_name = "incident_add.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAddSuccess(GroupLoginRequiredMixin, View):
    template_name = "incident_add_success.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        return render(_request, self.template_name, {})


class VoucherCancel(GroupLoginRequiredMixin, View):
    template_name = "voucher/cancel.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _pk):
        req = get_object_or_404(IncidenceDocument, pk=_pk)
        context = {
            'req': req
        }
        return render(_request, self.template_name, context)

    def post(self, _request, _pk):
        req = get_object_or_404(IncidenceDocument, pk=_pk)
        req.updated_by = _request.user.profile
        req.status = "can"
        req.save()
        return redirect(reverse('payroll:voucher_list_all'))


class IncidentView(GroupLoginRequiredMixin, View):
    template_name = "incident_view.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class IncidentEdit(GroupLoginRequiredMixin, View):
    template_name = "incident_edit.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class IncidentCancel(View):
    template_name = "incident_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
