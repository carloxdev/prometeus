# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import IncidentType
from .models import IncidentReport


@admin.register(IncidentType)
class IncidentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_date',
        'updated_date',
    )


@admin.register(IncidentReport)
class IncidentReport(admin.ModelAdmin):
    list_display = (
        'id',
        'employee',
        'type',
        'date',
        'reason',
        'response',
        'status',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )
