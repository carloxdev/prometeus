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
from django.contrib import messages


# Own's Libraries
from security.mixins import GroupLoginRequiredMixin
from .business import IncidentReportBusiness as IncidentBusiness
from .models import IncidentReport
from .forms import IncidentReportAddForm
from .forms import IncidentReportEditForm


class IncidentListView(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_review.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')

        if _status == 'pending':
            records = IncidentBusiness.get_Pending(
                query,
                _request.user.profile
            )
        else:
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


class IncidentListEdit(GroupLoginRequiredMixin, View):
    template_name = "incident/list_for_edit.html"
    group = ['INCIDENCIAS_ADM', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')

        if _status == 'pending':
            records = IncidentBusiness.get_Pending(query)
        else:
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

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile

        if form.instance.type.evidence_required:
            form.instance.status = 'inc'
        else:
            form.instance.status = 'pen'

        response = super(IncidentAdd, self).form_valid(form)
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'labor:incident_add_evidence',
            args=(self.object.pk,)
        )


class IncidentAddEvidence(GroupLoginRequiredMixin, View):
    template_name = "incident/add_evidence.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request, pk):
        record = get_object_or_404(IncidentReport, pk=pk)
        evidences = record.incidentevidence_set.all()
        context = {
            'record': record,
            'evidences': evidences
        }
        return render(_request, self.template_name, context)

    def post(self, _request, pk):
        record = get_object_or_404(IncidentReport, pk=pk)
        evidences = record.incidentevidence_set.all()

        if record.type.evidence_required:
            if len(evidences) > 0:
                return redirect(reverse('labor:incident_list_all'))
            else:
                messages.error(
                    _request,
                    "Se require al menos una imagen de evidencia"
                )
        else:
            return redirect(reverse('labor:incident_list_all'))

        context = {
            'record': record,
            'evidences': evidences
        }

        return render(_request, self.template_name, context)


class IncidentAddSuccess(GroupLoginRequiredMixin, TemplateView):
    template_name = "incident/add_success.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]


class IncidentCancel(GroupLoginRequiredMixin, View):
    template_name = "incident/cancel.html"
    group = ['INCIDENCIAS_ADM', 'INCIDENCIAS_USR', ]

    def get(self, _request, pk):
        record = get_object_or_404(IncidentReport, pk=pk)
        context = {
            'record': record
        }
        return render(_request, self.template_name, context)

    def post(self, _request, pk):
        record = get_object_or_404(IncidentReport, pk=pk)
        record.updated_by = _request.user.profile
        record.status = "can"
        record.save()
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
