# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import VoucherType
from .models import VoucherRequisition
from .models import BenefitType
from .models import BenefitRequisition


@admin.register(VoucherType)
class VoucherTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'valid_range',
        'created_date',
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
        'created_date',
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
