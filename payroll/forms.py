# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import ModelForm
from django.forms import Select
# from django.forms import TextInput
from django.forms import FileInput
from django.forms import DateInput
from django.forms import Textarea
from django.forms import ValidationError

# Own's Libraries
from .models import VoucherRequisition, BenefitRequisition


class VoucherRequisitionAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VoucherRequisitionAddForm, self).__init__(*args, **kwargs)
        self.fields['reason'].required = True

    class Meta:
        model = VoucherRequisition
        fields = (
            'type',
            'date_start',
            'date_end',
            'reason',
        )
        exclude = [
            'employee',
            'response',
            'is_complete',
        ]

        widgets = {
            'date_start': DateInput(
                attrs={'class': 'form-control'},
                format='%d/%m/%Y'
            ),
            'date_end': DateInput(
                attrs={'class': 'form-control'},
                format='%d/%m/%Y'
            ),
            'type': Select(attrs={'class': 'form-control'}),
            'reason': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
        }

        labels = {
            'type': 'Tipo de comprobante:',
            'reason': 'Motivo:'
        }

    # def clean_date_end(self):
    #     date_start = self.cleaned_data['date_start']
    #     date_end = self.cleaned_data['date_end']
    #
    #     if date_end < date_start:
    #         raise ValidationError(
    #             "La fecha final no puede ser menor a la inicial"
    #         )
    #
    #     return date_end


# class VoucherRequisitionCancel(ModelForm):
#     class Meta:
#         model = VoucherRequisition
#         fields = (
#             ''
#         )
#


class VoucherRequisitionEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VoucherRequisitionEditForm, self).__init__(*args, **kwargs)
        instance = kwargs['instance']
        if instance.status == 'can' or instance.status == 'com':
            self.fields['status'].widget.attrs['readonly'] = True
            self.fields['file'].widget.attrs['readonly'] = True
            self.fields['response'].widget.attrs['readonly'] = True

    class Meta:
        model = VoucherRequisition
        fields = (
            'file',
            'status',
            'response',
        )
        exclude = [
            'employee',
            'type',
            'date_start',
            'date_end',
            'reason',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date',
        ]
        widgets = {
            'file': FileInput(attrs={
                'class': 'filestyle',
                'data-iconName': 'glyphicon glyphicon-file',
                'data-buttonText': 'Seleccionar Archivo'
            }),
            'status': Select(attrs={'class': 'form-control'}),
            'response': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
        }
        labels = {
            'file': 'Archivo',
            'status': 'Estado',
            'response': 'Respuesta',
        }

    def clean(self):
        status = self.cleaned_data['status']
        file = self.cleaned_data['file']
        response = self.cleaned_data['response']

        if status == "com" and file is None:
            raise ValidationError(
                "No se puede marcar como Completado sin adjuntar un archivo"
            )

        if status == "can" and response == "":
            raise ValidationError(
                "Favor de dar explicar porque estas cancelando la solicitud"
            )


class BenefitRequisitionAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BenefitRequisitionAddForm, self).__init__(*args, **kwargs)
        self.fields['reason'].required = True

    class Meta:
        model = BenefitRequisition
        fields = (
            'type',
            'date',
            'reason',
        )
        widgets = {
            'date': DateInput(
                attrs={'class': 'form-control'},
                format='%d/%m/%Y'
            ),
            'type': Select(attrs={'class': 'form-control'}),
            'reason': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
        }

        labels = {
            'type': 'Tipo de Prestacion:',
            'reason': 'Motivo:'
        }


class BenefitRequisitionEditForm(ModelForm):
    user_fields = ['payment_evidence', ]  # Fill with user fillable fields.

    def __init__(self, is_admin_form=False, is_cancelled=False, *args, **kwargs):
        super(BenefitRequisitionEditForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
        if not is_cancelled:
            if is_admin_form:
                for field in [x for x in self.fields if x in self.user_fields]:
                    self.fields[field].widget.attrs['readonly'] = True
            else:
                for field in [x for x in self.fields if not x in self.user_fields]:
                    self.fields[field].widget.attrs['readonly'] = True
        else:
            for field in self.fields:
                self.fields[field].widget.attrs['readonly'] = True

    class Meta:
        model = BenefitRequisition
        fields = [
            "payment_info",
            'status',
            'payment_evidence',
            'admin_response',
        ]
        widgets = {
            "payment_info": Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            "admin_response": Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            "payment_evidence": Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            'status': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "payment_info": 'Información del pago',
            "payment_evidence": 'Evidencia del pago',
            "admin_response": 'Respuesta del administrador',
            'status': 'Estado de la operación',
        }
