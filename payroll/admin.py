# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import TipoComprobante
from .models import SolicitudComprobante


@admin.register(TipoComprobante)
class TipoComprobanteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'descripcion',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )


@admin.register(SolicitudComprobante)
class SolicitudComprobanteAdmin(admin.ModelAdmin):
    list_display = (
        'empleado',
        'tipo',
        'fecha_inicial',
        'fecha_final',
        'motivo',
        'respuesta',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )
