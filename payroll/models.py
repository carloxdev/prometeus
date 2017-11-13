# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from django.utils.translation import ugettext_lazy as lazy

# Own's Libraries
from security.models import Profile


class TipoComprobante(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    descripcion = models.CharField(max_length=144, blank=True, null=True)

    created_by = models.ForeignKey(
        Profile,
        related_name='tc_creador',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_by = models.ForeignKey(
        Profile,
        related_name='tc_actualizador',
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
        return self.nombre


class SolicitudComprobante(models.Model):
    empleado = models.ForeignKey(
        Profile,
        blank=False,
        on_delete=models.PROTECT
    )
    tipo = models.ForeignKey(
        TipoComprobante,
        blank=False,
        on_delete=models.PROTECT
    )
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    motivo = models.TextField(max_length=144, blank=True)
    respuesta = models.TextField(max_length=144, blank=True)
    is_complete = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        Profile,
        related_name='sc_creador',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_by = models.ForeignKey(
        Profile,
        related_name='sc_actualizador',
        blank=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name_plural = lazy('Solicitudes de Comprobantes')

    def __unicode__(self):
        desc = "%s : %s - %s" % (self.pk, self.empleado, self.tipo)
        return desc
