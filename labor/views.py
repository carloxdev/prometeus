# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View


class IncidentListPending(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAll(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAdminPending(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentListAdminAll(View):
    template_name = "incident_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAdd(View):
    template_name = "incident_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentAddSuccess(View):
    template_name = "incident_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class IncidentView(View):
    template_name = "incident_view.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class IncidentEdit(View):
    template_name = "incident_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class IncidentCancel(View):
    template_name = "incident_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
