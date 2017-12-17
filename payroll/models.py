# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Own's Libraries
from .utilities import Helper
from security.models import Profile
from social.business import CommentBusiness


class VoucherType(models.Model):
    name = models.CharField(
        "Nombre",
        max_length=50,
        blank=False,
        unique=True
    )
    description = models.TextField("Descripción", blank=True, null=True)

    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = 'Tipo de Comprobante'
        verbose_name_plural = 'Tipos de Comprobantes'

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
        verbose_name="Empleado",
        blank=False,
        on_delete=models.PROTECT
    )
    type = models.ForeignKey(
        VoucherType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    date_start = models.DateField("Fecha Inicio")
    date_end = models.DateField("Fecha Fin")
    reason = models.TextField("Motivo de la Solicitud", blank=True)
    response = models.TextField("Respuesta de Administracion", blank=True)
    file = models.FileField(
        "Archivo",
        upload_to=Helper.get_FilePath_Voucher,
        validators=[
            Helper.validate_Size
        ],
        blank=True,
        null=True,
    )
    status = models.CharField(
        "Estado",
        max_length=3,
        choices=STATUS_OPTIONS,
        default="pen"
    )
    created_by = models.ForeignKey(
        Profile,
        verbose_name="Creado por",
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
        verbose_name="Actualizado por",
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
        verbose_name = 'Solicitud de Comprobante'
        verbose_name_plural = 'Solicitudes de Comprobantes'

    def __unicode__(self):
        desc = "%s : %s - %s" % (self.pk, self.employee, self.type)
        return desc

    @property
    def is_Complete(self):
        if self.status == "com":
            return True
        else:
            return False

    @property
    def is_Cancel(self):
        if self.status == "can":
            return True
        else:
            return False

    @property
    def comments(self):
        records = CommentBusiness.get(self.__class__, self.id)
        return records


class BenefitType(models.Model):
    name = models.CharField(
        "Nombre",
        max_length=50,
        blank=False,
        unique=True
    )
    description = models.TextField("Descripción", blank=True, null=True)

    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = 'Tipo de Prestacion'
        verbose_name_plural = 'Tipos de Prestaciones'

    def __unicode__(self):
        return self.name


class BenefitRequisition(models.Model):
    STATUS = (
        ('pen', 'Pendiente'),
        ('ppe', 'Pago Pendiente'),
        ('ppc', 'Pago Por Comprobar'),
        ('com', 'Completado'),
    )

    employee = models.ForeignKey(
        Profile,
        verbose_name="Empleado",
        blank=False,
        on_delete=models.PROTECT
    )
    type = models.ForeignKey(
        BenefitType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    date = models.DateField("Fecha")
    reason = models.TextField("Motivo de la Solicitud", blank=True)
    payment_evidence = models.TextField("Evidencia del Pago", blank=True)
    admin_response = models.TextField(
        "Respuesta de Administración",
        blank=True
    )
    payment_info = models.TextField("Informacion del Pago", blank=True)
    status = models.CharField(
        "Estado", max_length=3, choices=STATUS, default="pen")
    created_by = models.ForeignKey(
        Profile,
        verbose_name="Creado por",
        related_name='sp_created_by',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_by = models.ForeignKey(
        Profile,
        verbose_name="Actualizado por",
        related_name='sp_updated_by',
        blank=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = 'Solicitud de Prestacion'
        verbose_name_plural = 'Solicitudes de Prestaciones'

    def __unicode__(self):
        desc = "%s : %s - %s" % (self.pk, self.employee, self.type)
        return desc

    @property
    def comments(self):
        records = CommentBusiness.get(self.__class__, self.id)
        return records
