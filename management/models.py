# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models

# Own's Libraries
from security.models import Profile
from labor.models import IncidentType
from payroll.models import VoucherType
from payroll.models import BenefitType


class IncidentConfig(models.Model):
    type = models.ForeignKey(
        IncidentType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    email = models.EmailField()
    user = models.ForeignKey(
        Profile,
        verbose_name="administrador",
        related_name='admin_incident',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        unique_together = (('type', 'email'),)
        verbose_name = 'Configuración de Incidencias'
        verbose_name_plural = 'Configuraciones de Incidencias'

    def __unicode__(self):
        return self.type.name


class VoucherConfig(models.Model):
    type = models.ForeignKey(
        VoucherType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    email = models.EmailField()
    user = models.ForeignKey(
        Profile,
        verbose_name="administrador",
        related_name='admin_voucher',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        unique_together = (('type', 'email'),)
        verbose_name = 'Configuración de Comprobantes'
        verbose_name_plural = 'Configuraciones de Comprobantes'

    def __unicode__(self):
        return self.type.name


class BenefitConfig(models.Model):
    type = models.ForeignKey(
        BenefitType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    email = models.EmailField()
    user = models.ForeignKey(
        Profile,
        verbose_name="administrador",
        related_name='admin_benefit',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        unique_together = (('type', 'email'),)
        verbose_name = 'Configuración de Beneficios'
        verbose_name_plural = 'Configuraciones de Beneficios'

    def __unicode__(self):
        return self.type.name
