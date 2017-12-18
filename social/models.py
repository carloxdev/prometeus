# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Own's Libraries
from security.models import Profile


class Comment(models.Model):

    limit = models.Q(app_label='labor', model='IncidentDocument') | \
            models.Q(app_label='payroll', model='VoucherRequisition') | \
            models.Q(app_label='payroll', model='BenefitRequisition')

    content = models.TextField('contenido')
    created_by = models.ForeignKey(
        Profile,
        related_name='comments_created_by',
        blank=True,
        null=True,
        verbose_name="creado por",
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
        verbose_name="Tabla"
    )
    object_id = models.PositiveIntegerField("clave del registro")
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
