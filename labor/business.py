# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Own's Libraries
from .models import IncidentReport


class IncidentReportBusiness(object):

    @classmethod
    def get(self, _pk):
        requisition = get_object_or_404(IncidentReport, pk=_pk)
        return requisition

    @classmethod
    def get_No_Pendings(self):
        quantity = IncidentReport.objects.filter(
            status__in=["pen", 'inc']).count()
        return quantity

    @classmethod
    def get_FilterByEmployee(self, _value, _profile):
        if _value:
            records = IncidentReport.objects \
                .filter(employee=_profile) \
                .filter(
                    Q(type__name__icontains=_value) |
                    Q(reason__icontains=_value)
                ).order_by("-created_date")
        else:
            records = IncidentReport.objects \
                .filter(employee=_profile) \
                .order_by("-created_date")

        return records

    @classmethod
    def get_Pending(self, _value, _profile=None):
        if _value:
            records = IncidentReport.objects \
                .filter(
                    Q(type__name__icontains=_value) |
                    Q(pk__icontains=_value) |
                    Q(reason__icontains=_value) |
                    Q(response__icontains=_value) |
                    Q(employee__user__first_name__icontains=_value) |
                    Q(employee__user__last_name__icontains=_value)
                ) \
                .filter(status__in=["pen", 'inc']) \
                .order_by("-created_date")
        else:
            records = IncidentReport.objects \
                .filter(status__in=["pen", 'inc']) \
                .order_by("-created_date")

        if _profile:
            records = records.filter(employee=_profile)

        return records

    @classmethod
    def get_All(self, _value, _profile=None):
        if _value:
            records = IncidentReport.objects \
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
            records = IncidentReport.objects \
                .order_by("-created_date")

        if _profile:
            records = records.filter(employee=_profile)

        return records

    @classmethod
    def get_Paginated(self, _records, _current_page):
        paginator = Paginator(_records, 10)
        current_pagina = _current_page

        try:
            _records = paginator.page(current_pagina)
        except PageNotAnInteger:
            _records = paginator.page(1)
        except EmptyPage:
            _records = paginator.page(paginator.num_page)

        return _records
