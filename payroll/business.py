# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Own's Libraries
from .models import SolicitudComprobante


class SolicitudComprobanteBusiness(object):

    @classmethod
    def get(self, _pk):
        solicitud = get_object_or_404(SolicitudComprobante, pk=_pk)
        return solicitud

    @classmethod
    def get_FilterBy(self, _value, _profile):
        if _value:
            users = SolicitudComprobante.objects \
                .filter(created_by=_profile) \
                .filter(
                    Q(tipo__nombre__icontains=_value) |
                    Q(motivo__icontains=_value)
                ).order_by("-created_date")
        else:
            users = SolicitudComprobante.objects \
                .filter(created_by=_profile) \
                .order_by("-created_date")

        return users

    @classmethod
    def get_Paginated(self, _users, _current_page):
        paginator = Paginator(_users, 20)
        current_pagina = _current_page

        try:
            _users = paginator.page(current_pagina)
        except PageNotAnInteger:
            _users = paginator.page(1)
        except EmptyPage:
            _users = paginator.page(paginator.num_page)

        return _users
