# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals
import os

# Django's Libraries
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as lazy
from django.utils.translation import gettext_lazy as _

# Own's Libraries
from home.utilities import Helper
from security.models import Profile
from social.business import CommentBusiness


def get_FilePath_Voucher(_instance, _filename):

    if (_instance):
        upload_dir = os.path.join(
            'files',
            'vouchers',
        )
    return os.path.join(upload_dir, _filename)


class VoucherType(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        Profile,
        related_name='tc_created_by',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_by = models.ForeignKey(
        Profile,
        related_name='tc_updated_by',
        blank=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name_plural = lazy('Tipos de Comprobante')

    def __unicode__(self):
        return self.name


class VoucherRequisition(models.Model):

    STATUS_OPTIONS = (
        ('pen', 'PENDIENTE'),
        ('can', 'CANCELADO'),
        ('com', 'COMPLETADO'),
    )

    employee = models.ForeignKey(
        Profile,
        blank=False,
        on_delete=models.PROTECT
    )
    type = models.ForeignKey(
        VoucherType,
        blank=False,
        on_delete=models.PROTECT
    )
    date_start = models.DateField()
    date_end = models.DateField()
    reason = models.TextField(blank=True)
    response = models.TextField(blank=True)
    file = models.FileField(
        upload_to=get_FilePath_Voucher,
        validators=[
            Helper.validate_Size
        ],
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_OPTIONS,
        default="pen"
    )
    created_by = models.ForeignKey(
        Profile,
        related_name='sc_created_by',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_by = models.ForeignKey(
        Profile,
        related_name='sc_updated_by',
        blank=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    def clean(self):
        fecha_inicio = self.date_start
        fecha_fin = self.date_end

        if fecha_fin < fecha_inicio:
            raise ValidationError({
                'date_end': _(
                    'Fecha final no puede ser menor que fecha inicial.'
                )
            })

    class Meta:
        verbose_name_plural = lazy('Solicitudes de Comprobantes')

    def __unicode__(self):
        desc = "%s : %s - %s" % (self.pk, self.employee, self.type)
        return desc

    @property
    def is_Complete(self):
        if self.status == "com":
            return True
        else:
            return False
    # is_Complete = property(_is_Complete)

    @property
    def is_Cancel(self):
        if self.status == "can":
            return True
        else:
            return False
    # is_Cancel = property(_is_Cancel)

    @property
    def comments(self):
        records = CommentBusiness.get(self.__class__, self.id)
        return records
