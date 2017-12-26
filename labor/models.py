# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models

# Third-party Libraries
from django_resized import ResizedImageField

# Own's Libraries
from security.models import Profile
from social.business import CommentBusiness
from .utilities import Helper


class IncidentType(models.Model):
    name = models.CharField(
        "Nombre",
        max_length=50,
        blank=False,
        unique=True
    )
    description = models.TextField("Descripción", blank=True, null=True)
    evidence_required = models.BooleanField("Requerir evidencia", default=True)

    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = 'Tipo de Incidencia'
        verbose_name_plural = 'Tipos de Incidencia'

    def __unicode__(self):
        return self.name


class IncidentReport(models.Model):
    STATUS_OPTIONS = (
        ('inc', 'INCOMPLETO'),
        ('pen', 'PENDIENTE'),
        ('can', 'CANCELADO'),
        ('com', 'PROCESADO'),
    )

    employee = models.ForeignKey(
        Profile,
        verbose_name="Empleado",
        blank=False,
        on_delete=models.PROTECT
    )
    type = models.ForeignKey(
        IncidentType,
        verbose_name="Tipo",
        blank=False,
        on_delete=models.PROTECT
    )
    date = models.DateField("Fecha", blank=True, null=True)
    reason = models.TextField("Motivo de la Solicitud", blank=True)
    response = models.TextField("Respuesta de Administracion", blank=True)
    file = models.FileField(
        "Archivo",
        upload_to=Helper.get_FilePath_Incident,
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
        related_name='si_created_by',
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
        related_name='si_updated_by',
        blank=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = 'Reporte de Incidencia'
        verbose_name_plural = 'Reportes de Incidencias'

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


class IncidentEvidence(models.Model):
    incident = models.ForeignKey(
        IncidentReport,
        verbose_name="Reporte de Incidencia",
        blank=True,
        null=True
    )
    image = ResizedImageField(
        "Foto",
        upload_to=Helper.get_ImagePath_Evidence,
        quality=75,
        blank=True,
        keep_meta=False,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
