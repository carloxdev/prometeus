# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View


class IncidentList(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAdd(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAddSuccess(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentEdit(View):
    template_name = "incident_list.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
