# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import ModelForm
from django.forms import Select
# from django.forms import TextInput
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
            'employee',
            'type',
            'date_start',
            'date_end',
            'reason',
        )
        exclude = [
            'response',
            'is_complete',
        ]

        widgets = {
            'employee': Select(attrs={'class': 'form-control'}),
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
            'employee': 'Empleado:',
            'type': 'Tipo de comprobante:',
            'reason': 'Motivo:'
        }

    def clean_date_end(self):
        date_start = self.cleaned_data['date_start']
        date_end = self.cleaned_data['date_end']

        if date_end < date_start:
            raise ValidationError(
                "La fecha final no puede ser menor a la inicial"
            )

        return date_end
