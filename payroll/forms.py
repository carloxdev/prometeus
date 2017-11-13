# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import ModelForm


# Own's Libraries
from .models import SolicitudComprobante


class SolicitudComprobanteForm(ModelForm):

    class Meta:
        model = SolicitudComprobante
        fields = (
            'empleado',
            'tipo',
            'fecha_inicial',
            'fecha_final',
            'motivo',
            'respuesta',
            'is_complete',
        )
