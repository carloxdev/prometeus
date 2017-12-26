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
from .models import IncidentReport
from .models import IncidentEvidence


class IncidentReportAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(IncidentReportAddForm, self).__init__(*args, **kwargs)
        self.fields['reason'].required = True
        self.fields['date'].required = True

    class Meta:
        model = IncidentReport
        fields = (
            'type',
            'date',
            'reason',
        )
        exclude = [
            'employee',
            'response',
            'is_complete',
        ]

        widgets = {
            'date': DateInput(
                attrs={'class': 'form-control'},
                format='%d/%m/%Y'
            ),
            'type': Select(attrs={'class': 'form-control'}),
            'reason': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
        }

        labels = {
            'type': 'Tipo de comprobante:',
            'reason': 'Descripción:'
        }


class IncidentReportEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncidentReportEditForm, self).__init__(*args, **kwargs)
        instance = kwargs['instance']
        if instance.status == 'can' or instance.status == 'com':
            self.fields['status'].widget.attrs['readonly'] = True
            self.fields['file'].widget.attrs['readonly'] = True
            self.fields['response'].widget.attrs['readonly'] = True

    class Meta:
        model = IncidentReport
        fields = (
            'file',
            'status',
            'response',
        )
        exclude = [
            'employee',
            'type',
            'date',
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


class IncidentEvidenceAddForm(ModelForm):
    class Meta:
        model = IncidentEvidence
        fields = ('incident', 'image')
