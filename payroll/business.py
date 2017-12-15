# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Own's Libraries
from .models import VoucherRequisition


class VoucherRequisitionBusiness(object):

    @classmethod
    def get(self, _pk):
        requisition = get_object_or_404(VoucherRequisition, pk=_pk)
        return requisition

    @classmethod
    def get_No_Pending(self):
        cantidades = VoucherRequisition.objects.filter(status="pen").count()
        return cantidades

    @classmethod
    def get_FilterByEmployee(self, _value, _profile):
        if _value:
            requisitions = VoucherRequisition.objects \
                .filter(employee=_profile) \
                .filter(
                    Q(type__name__icontains=_value) |
                    Q(reason__icontains=_value)
                ).order_by("-created_date")
        else:
            requisitions = VoucherRequisition.objects \
                .filter(employee=_profile) \
                .order_by("-created_date")

        return requisitions

    @classmethod
    def get_Pending(self, _value, _profile=None):
        if _value:
            requisitions = VoucherRequisition.objects \
                .filter(
                    Q(type__name__icontains=_value) |
                    Q(pk__icontains=_value) |
                    Q(reason__icontains=_value) |
                    Q(response__icontains=_value) |
                    Q(employee__user__first_name__icontains=_value) |
                    Q(employee__user__last_name__icontains=_value)
                ) \
                .filter(status="pen") \
                .order_by("-created_date")
        else:
            requisitions = VoucherRequisition.objects \
                .filter(status="pen") \
                .order_by("-created_date")

        if _profile:
            requisitions = requisitions.filter(employee=_profile)

        return requisitions

    @classmethod
    def get_All(self, _value, _profile=None):
        if _value:
            requisitions = VoucherRequisition.objects \
                .filter(
                    Q(type__name__icontains=_value) |
                    Q(pk__icontains=_value) |
                    Q(reason__icontains=_value) |
                    Q(response__icontains=_value) |
                    Q(employee__user__first_name__icontains=_value) |
                    Q(employee__user__last_name__icontains=_value)
                ) \
                .order_by("-created_date")
        else:
            requisitions = VoucherRequisition.objects \
                .order_by("-created_date")

        if _profile:
            requisitions = requisitions.filter(employee=_profile)

        return requisitions

    @classmethod
    def get_Paginated(self, _requisitions, _current_page):
        paginator = Paginator(_requisitions, 20)
        current_pagina = _current_page

        try:
            _requisitions = paginator.page(current_pagina)
        except PageNotAnInteger:
            _requisitions = paginator.page(1)
        except EmptyPage:
            _requisitions = paginator.page(paginator.num_page)

        return _requisitions
