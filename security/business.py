# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Third-party Libraries
import xlwt

# Own's Libraries
from .models import Profile


class UserBusiness(object):

    @classmethod
    def get(self, _pk):
        user = get_object_or_404(User, pk=_pk)
        return user

    @classmethod
    def get_Profile(self, _pk):
        profile = get_object_or_404(Profile, pk=_pk)
        return profile

    @classmethod
    def get_FilterBy(self, _value):
        if _value:
            users = User.objects.filter(
                Q(username__icontains=_value) |
                Q(first_name__icontains=_value) |
                Q(last_name__icontains=_value)
            ).order_by("-date_joined")
        else:
            users = User.objects.all().order_by("-date_joined")

        return users

    @classmethod
    def get_Paginated(self, _users, _current_page):
        paginator = Paginator(_users, 10)
        current_pagina = _current_page

        try:
            _users = paginator.page(current_pagina)
        except PageNotAnInteger:
            _users = paginator.page(1)
        except EmptyPage:
            _users = paginator.page(paginator.num_page)

        return _users

    @classmethod
    def get_ExcelData(self, _users):

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Infomacion')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()

        columns = [
            'Numero',
            'Nombre(s)',
            'Apellido(s)',
            'Email',
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        for row in _users:
            row_num += 1

            ws.write(row_num, 0, row.username, font_style)
            ws.write(row_num, 1, row.first_name, font_style)
            ws.write(row_num, 2, row.last_name, font_style)
            ws.write(row_num, 3, row.email, font_style)

        return wb
