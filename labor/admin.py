# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import IncidentType
from .models import IncidentReport
from .models import IncidentEvidence


@admin.register(IncidentType)
class IncidentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_date',
        'updated_date',
    )


class IncidentEvidenceline(admin.TabularInline):
    model = IncidentEvidence
    extra = 1


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
    inlines = (
        IncidentEvidenceline,
    )
