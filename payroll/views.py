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
# from django.views.generic import ListView
from django.urls import reverse_lazy

# Own's Libraries
from security.mixins import GroupLoginRequiredMixin

from .business import VoucherRequisitionBusiness as VoucherBusiness
from .models import VoucherRequisition
from .forms import VoucherRequisitionAddForm
from .forms import VoucherRequisitionEditForm


class VoucherList(GroupLoginRequiredMixin, View):
    template_name = "voucher/list.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_Pendientes(
            query,
            _request.user.profile
        )
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherListAll(GroupLoginRequiredMixin, View):
    template_name = "voucher/list.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_All(
            query,
            _request.user.profile
        )
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherListAdmin(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_admin.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_Pendientes(query)
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherListAdminAll(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_admin.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_All(query)
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherAdd(GroupLoginRequiredMixin, CreateView):
    template_name = "voucher/add.html"
    model = VoucherRequisition
    form_class = VoucherRequisitionAddForm
    success_url = reverse_lazy('payroll:voucher_add_success')

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        return super(VoucherAdd, self).form_valid(form)


class VoucherAddSuccess(TemplateView):
    template_name = "voucher/add_success.html"


class VoucherCancel(View):
    template_name = "voucher/cancel.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _pk):
        req = get_object_or_404(VoucherRequisition, pk=_pk)
        context = {
            'req': req
        }
        return render(_request, self.template_name, context)

    def post(self, _request, _pk):
        req = get_object_or_404(VoucherRequisition, pk=_pk)
        req.updated_by = _request.user.profile
        req.status = "can"
        req.save()
        return redirect(reverse('payroll:voucher_list_all'))


class VoucherView(DetailView):
    model = VoucherRequisition
    template_name = "voucher/view.html"
    context_object_name = "rq"

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(VoucherView, self).get_context_data(**context)


class VoucherEdit(UpdateView):
    model = VoucherRequisition
    template_name = "voucher/edit_admin.html"
    form_class = VoucherRequisitionEditForm
    success_url = reverse_lazy('payroll:voucher_list_admin')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.profile
        return super(VoucherEdit, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = {}
    #     if self.object:
    #         context['object'] = self.object
    #         context_object_name = self.get_context_object_name(self.object)
    #         if context_object_name:
    #             context[context_object_name] = self.object
    #
    #
    #     context.update(kwargs)
    #     return super(VoucherEdit, self).get_context_data(**context)


class BenefitList(View):
    template_name = "benefit_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitAdd(View):
    template_name = "benefit_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitAddSuccess(View):
    template_name = "benefit_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitView(View):
    template_name = "benefit_view.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class BenefitEdit(View):
    template_name = "benefit_edit.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})
