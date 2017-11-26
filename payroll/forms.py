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
from .models import VoucherRequisition


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
