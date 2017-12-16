# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import VoucherType, BenefitRequisition, BenefitType
from .models import VoucherRequisition


@admin.register(VoucherType)
class VoucherTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )


@admin.register(VoucherRequisition)
class VoucherRequisitionAdmin(admin.ModelAdmin):
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


@admin.register(BenefitType)
class BenefitTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )


@admin.register(BenefitRequisition)
class BenefitRequisitionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employee',
        'type',
        'date',
        'reason',
        'payment_info',
        'status',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )
