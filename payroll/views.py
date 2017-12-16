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
from .business import BenefitRequisitionBusiness as BenefitBusiness
from .models import VoucherRequisition, BenefitRequisition
from .forms import VoucherRequisitionAddForm, BenefitRequisitionAddForm, BenefitRequisitionEditForm
from .forms import VoucherRequisitionEditForm


class VoucherListPending(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_for_review.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_Pending(
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
    template_name = "voucher/list_for_review.html"
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


class VoucherListAdminPending(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_for_edit.html"
    group = ['COMPROBANTES_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = VoucherBusiness.get_Pending(query)
        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherListAdminAll(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_for_edit.html"
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
    template_name = "voucher/edit.html"
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
    group = ['PRESTACIONES_ADM', 'PRESTACIONES_USR', ]

    def get(self, _request):
        query = _request.GET.get('q')
        requisitions = BenefitBusiness.get_Pendientes(
            query,
            _request.user.profile
        )
        requisitions_paginated = BenefitBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'requisitions': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class BenefitAdd(CreateView):
    template_name = "benefit_add.html"
    model = BenefitRequisition
    form_class = BenefitRequisitionAddForm
    success_url = reverse_lazy('payroll:benefit_add_success')

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        return super(BenefitAdd, self).form_valid(form)


class BenefitAddSuccess(View):
    template_name = "benefit_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitEdit(View):
    template_name = "benefit_edit.html"
    group = ['PRESTACIONES_ADM', 'PRESTACIONES_USR', ]

    def get(self, request, pk):
        benefit = get_object_or_404(BenefitRequisition, pk=pk)
        is_admin_form = (request.user.groups.filter(
            name='PRESTACIONES_ADM').exists() or request.user.is_superuser) and benefit.created_by.user != request.user

        form = BenefitRequisitionEditForm(instance=benefit, is_admin_form=is_admin_form)
        context = {
            'rq': benefit,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        benefit = get_object_or_404(BenefitRequisition, pk=pk)
        form = BenefitRequisitionEditForm(data=request.POST, instance=benefit)

        if form.is_valid():
            form.save()
            return redirect('payroll:benefit_add_success')
        else:
            return redirect(reverse('payroll:benefit_edit'), pk=pk)

