# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import IncidentConfig
from .models import VoucherConfig
from .models import BenefitConfig


@admin.register(IncidentConfig)
class IncidentConfigAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'email',
        'user',
        'created_date',
        'updated_date',
    )

    class Meta:
        verbose_name = 'Configuracion Incidentes'
        verbose_name_plural = 'Configuraciones de Incidentes'


@admin.register(VoucherConfig)
class VoucherConfigAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'email',
        'user',
        'created_date',
        'updated_date',
    )

    class Meta:
        verbose_name = 'Configuracion Comprobantes'
        verbose_name_plural = 'Configuraciones de Comprobantes'


@admin.register(BenefitConfig)
class BenefitConfigAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'email',
        'user',
        'created_date',
        'updated_date',
    )

    class Meta:
        verbose_name = 'Configuracion Beneficios'
        verbose_name_plural = 'Configuraciones de Beneficios'
