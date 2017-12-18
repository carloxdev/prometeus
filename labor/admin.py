# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import IncidenceType
from .models import IncidenceDocument


@admin.register(IncidenceType)
class IncidenceTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_date',
        'updated_date',
    )


@admin.register(IncidenceDocument)
class IncidenceDocumentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employee',
        'type',
        'date_start',
        'date_end',
        'reason',
        'response',
        'status',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )
