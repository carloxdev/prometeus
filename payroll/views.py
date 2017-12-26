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
from management.postman import VoucherMail

from .models import VoucherRequisition
from .models import BenefitRequisition

from .business import VoucherRequisitionBusiness as VoucherBusiness
from .business import BenefitRequisitionBusiness as BenefitBusiness

from .forms import VoucherRequisitionAddForm
from .forms import VoucherRequisitionEditForm
from .forms import BenefitRequisitionAddForm
from .forms import BenefitRequisitionEditForm


class VoucherListView(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_for_review.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')

        if _status == 'pending':
            requisitions = VoucherBusiness.get_Pending(
                query,
                _request.user.profile
            )
        else:
            requisitions = VoucherBusiness.get_All(
                query,
                _request.user.profile
            )

        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'records': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherListEdit(GroupLoginRequiredMixin, View):
    template_name = "voucher/list_for_edit.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')

        if _status == 'pending':
            requisitions = VoucherBusiness.get_Pending(query)
        else:
            requisitions = BenefitBusiness.get_All(query)

        requisitions_paginated = VoucherBusiness.get_Paginated(
            requisitions,
            _request.GET.get('page')
        )
        context = {
            'records': requisitions_paginated
        }
        return render(_request, self.template_name, context)


class VoucherAdd(GroupLoginRequiredMixin, CreateView):
    template_name = "voucher/add.html"
    model = VoucherRequisition
    form_class = VoucherRequisitionAddForm
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]
    success_url = reverse_lazy('payroll:voucher_add_success')

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        response = super(VoucherAdd, self).form_valid(form)

        if response.status_code == 302:
            self.request.user.email_user(
                "Tu Solicitud con el no. %s fue CREADA correctamente" %
                (form.instance.pk),
                "La Administracion revisara tu solicitud "
                "y se te avisara por este medio cuando esta sea procesada."
            )

            VoucherMail.send(
                _type=form.instance.type,
                _subject="%s genero una nueva solicitud con el no. %s" % (
                    form.instance.employee.user.get_full_name(),
                    form.instance.pk
                ),
                _content="Estimado Administrador,\nEl empleado %s registro "
                "la solicitud #%s, solicitando un comprobante de %s. "
                "Favor de entrar a plataforma para revisar y procesar" %
                (
                    form.instance.employee.user.get_full_name(),
                    form.instance.pk,
                    form.instance.type.name
                )
            )

        return response


class VoucherAddSuccess(GroupLoginRequiredMixin, TemplateView):
    template_name = "voucher/add_success.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]


class VoucherCancel(GroupLoginRequiredMixin, View):
    template_name = "voucher/cancel.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]

    def get(self, _request, _pk):
        record = get_object_or_404(VoucherRequisition, pk=_pk)
        context = {
            'record': record
        }
        return render(_request, self.template_name, context)

    def post(self, _request, _pk):
        record = get_object_or_404(VoucherRequisition, pk=_pk)
        record.updated_by = _request.user.profile
        record.status = "can"
        record.save()

        record.employee.user.email_user(
            "Tu Solicitud con el no. %s fue CANCELADA correctamente" %
            (record.pk),
            "Se avisara a la Administracion para que no siga dando "
            "seguimiento a tu solicitud"
        )

        VoucherMail.send(
            _type=record.type,
            _subject="%s CANCELO la solicitud con el no. %s" % (
                record.employee.user.get_full_name(),
                record.pk
            ),
            _content="Estimado Administrador, \nSe CANCELO la solicitud #%s."
            "No es necesario que le siga dando seguimiento." %
            (record.pk),
        )

        return redirect(reverse('payroll:voucher_list_all'))


class VoucherView(GroupLoginRequiredMixin, DetailView):
    model = VoucherRequisition
    template_name = "voucher/view.html"
    group = ['COMPROBANTES_ADM', 'COMPROBANTES_USR', ]
    context_object_name = "record"


class VoucherEdit(GroupLoginRequiredMixin, UpdateView):
    model = VoucherRequisition
    template_name = "voucher/edit.html"
    group = ['COMPROBANTES_ADM', ]
    form_class = VoucherRequisitionEditForm
    success_url = reverse_lazy('payroll:voucher_list_admin_pending')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.profile
        response = super(VoucherEdit, self).form_valid(form)

        if response.status_code == 302:
            if form.instance.status == "can":
                form.instance.employee.user.email_user(
                    "La Administracion CANCELO tu solicitud con no. %s" %
                    (form.instance.pk),
                    "La Administracion CANCELO tu solicitud dejando el "
                    "siguiente motivo: \n - '%s'" % (
                        form.instance.response
                    )
                )

                VoucherMail.send(
                    _type=form.instance.type,
                    _subject="Se CANCELO la solicitud con el no. %s" %
                    (form.instance.pk),
                    _content="Estimado Administrador, \n"
                    "se CANCELO la solicitud #%s. "
                    "No es necesario que le siga dando seguimiento." %
                    (form.instance.pk)
                )

            elif form.instance.status == "com":
                form.instance.employee.user.email_user(
                    "La Administracion COMPLETO tu solicitud con no. %s" %
                    (form.instance.pk),
                    "La Administracion COMPLETO tu solicitud dejando el "
                    "siguiente mensaje: \n - '%s' \n - Archivo: %s" % (
                        form.instance.response,
                        "http://127.0.0.1:8000" + form.instance.file.url
                    )
                )

                VoucherMail.send(
                    _type=form.instance.type,
                    _subject="Se COMPLETO la solicitud con el no. %s" %
                    (form.instance.pk),
                    _content="Estimado Administrador, \n"
                    "se COMPLETO la solicitud #%s."
                    " No es necesario que le siga dando seguimiento." %
                    (form.instance.pk)
                )

        return response

    def form_invalid(self, form):
        # import ipdb; ipdb.set_trace()
        update_obj = VoucherRequisition.objects.get(id=form.instance.pk)
        form.instance = update_obj
        return self.render_to_response(self.get_context_data(form=form))


class BenefitListView(GroupLoginRequiredMixin, View):
    template_name = "benefit/list.html"
    group = ['PRESTACIONES_ADM', 'PRESTACIONES_USR', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')
        if _status == 'pending':
            requisitions = BenefitBusiness.get_Pendings(
                query, _request.user.profile)
        else:
            requisitions = BenefitBusiness.get_All(
                query, _request.user.profile)

        requisitions_paginated = BenefitBusiness.get_Paginated(
            requisitions, _request.GET.get('page'))

        context = {
            'status': _status,
            'requisitions': requisitions_paginated
        }

        return render(_request, self.template_name, context)


class BenefitListEdit(GroupLoginRequiredMixin, View):
    template_name = "benefit/list_admin.html"
    group = ['PRESTACIONES_ADM', ]

    def get(self, _request, _status):
        query = _request.GET.get('q')
        if _status == 'pending':
            requisitions = BenefitBusiness.get_Pendings(query)
        else:
            requisitions = BenefitBusiness.get_All(query)

        requisitions_paginated = BenefitBusiness.get_Paginated(
            requisitions, _request.GET.get('page'))

        context = {
            'status': _status,
            'requisitions': requisitions_paginated
        }

        return render(_request, self.template_name, context)


class BenefitAdd(CreateView):
    template_name = "benefit/add.html"
    model = BenefitRequisition
    form_class = BenefitRequisitionAddForm
    success_url = reverse_lazy('payroll:benefit_add_success')

    def form_valid(self, form):
        form.instance.employee = self.request.user.profile
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        response = super(BenefitAdd, self).form_valid(form)

        # if response.status_code == 302:
        #     self.request.user.email_user(
        #         "Esta chido",
        #         "Ejemplo de mensaje"
        #     )
        return response


class BenefitAddSuccess(View):
    template_name = "benefit/add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class BenefitEdit(View):
    template_name = "benefit/edit.html"
    group = ['PRESTACIONES_ADM', 'PRESTACIONES_USR', ]

    def get(self, request, pk):
        benefit = get_object_or_404(BenefitRequisition, pk=pk)
        is_admin_form = (request.user.groups.filter(name='PRESTACIONES_ADM').exists() or request.user.is_superuser) and benefit.created_by.user != request.user
        is_cancelled = benefit.status == 'can'
        form = BenefitRequisitionEditForm(
            instance=benefit,
            is_admin_form=is_admin_form,
            is_cancelled=is_cancelled
        )
        context = {
            'rq': benefit,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        benefit = get_object_or_404(BenefitRequisition, pk=pk)
        form = BenefitRequisitionEditForm(data=request.POST, instance=benefit)

        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            form.save()
            # request.user.email_user(
            #     "Esta chido",
            #     "Ejemplo de mensaje"
            # )
            return redirect('payroll:benefit_list_all')
        else:
            return redirect(reverse('payroll:benefit_edit', kwargs={'pk': pk}))


class BenefitCancel(GroupLoginRequiredMixin, View):
    template_name = "benefit/cancel.html"
    group = ['PRESTACIONES_ADM', 'PRESTACIONES_USR', ]

    def get(self, _request, pk):
        req = get_object_or_404(BenefitRequisition, pk=pk)
        context = {
            'req': req
        }
        return render(_request, self.template_name, context)

    def post(self, _request, pk):
        req = get_object_or_404(BenefitRequisition, pk=pk)
        req.updated_by = _request.user.profile
        req.status = "can"
        req.save()
        # _request.user.email_user(
        #     "Esta chido",
        #     "Ejemplo de mensaje"
        # )
        return redirect(reverse('payroll:benefit_list_all'))
