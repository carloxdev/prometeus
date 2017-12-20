# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# Own's Libraries
from security.mixins import GroupLoginRequiredMixin
from .business import IncidentReportBusiness as IncidentBusiness
from .models import IncidentReport
from .forms import IncidentReportAddForm
from .forms import IncidentReportEditForm


class IncidentListPending(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_review.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        records = IncidentBusiness.get_Pending(
            query,
            _request.user.profile
        )
        records_paginated = IncidentBusiness.get_Paginated(
            records,
            _request.GET.get('page')
        )
        context = {
            'records': records_paginated
        }
        return render(_request, self.template_name, context)


class IncidentListAll(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_review.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        records = IncidentBusiness.get_All(
            query,
            _request.user.profile
        )
        records_paginated = IncidentBusiness.get_Paginated(
            records,
            _request.GET.get('page')
        )
        context = {
            'records': records_paginated
        }
        return render(_request, self.template_name, context)


class IncidentListAdminPending(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_edit.html"
    group = ['INCIDENCIAS_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        records = IncidentBusiness.get_Pending(query)
        records_paginated = IncidentBusiness.get_Paginated(
            records,
            _request.GET.get('page')
        )
        context = {
            'records': records_paginated
        }
        return render(_request, self.template_name, context)


class IncidentListAdminAll(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_edit.html"
    group = ['INCIDENCIAS_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        records = IncidentBusiness.get_All(query)
        records_paginated = IncidentBusiness.get_Paginated(
            records,
            _request.GET.get('page')
        )
        context = {
            'records': records_paginated
        }
        return render(_request, self.template_name, context)


class IncidentAdd(GroupLoginRequiredMixin, CreateView):
    template_name = "incident/add.html"
    model = IncidentReport
    form_class = IncidentReportAddForm
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]
    success_url = reverse_lazy('labor:incident_add_success')

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        response = super(IncidentAdd, self).form_valid(form)

        if response.status_code == 302:
            self.request.user.email_user(
                "Esta chido",
                "Ejemplo de mensaje"
            )
        return response


class IncidentAddSuccess(GroupLoginRequiredMixin, TemplateView):
    template_name = "incident/add_success.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]


class IncidentCancel(GroupLoginRequiredMixin, View):
    template_name = "incident/cancel.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request, pk):
        req = get_object_or_404(IncidentReport, pk=pk)
        context = {
            'req': req
        }
        return render(_request, self.template_name, context)

    def post(self, _request, pk):
        req = get_object_or_404(IncidentReport, pk=pk)
        req.updated_by = _request.user.profile
        req.status = "can"
        req.save()
        return redirect(reverse('labor:incident_list_all'))


class IncidentView(GroupLoginRequiredMixin, DetailView):
    model = IncidentReport
    template_name = "incident/view.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]
    context_object_name = "record"

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(IncidentView, self).get_context_data(**context)


class IncidentEdit(GroupLoginRequiredMixin, UpdateView):
    model = IncidentReport
    template_name = "incident/edit.html"
    group = ['INCIDENCIAS_ADM', ]
    form_class = IncidentReportEditForm
    success_url = reverse_lazy('labor:incident_list_admin_pending')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.profile
        return super(IncidentEdit, self).form_valid(form)
