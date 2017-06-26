# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View


class NewList(View):
    template_name = "new_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class NewAdd(View):
    template_name = "new_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class NewAddSuccess(View):
    template_name = "new_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class NewView(View):
    template_name = "new_view.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class NewEdit(View):
    template_name = "new_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
