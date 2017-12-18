# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models

# Third-party Libraries
from django_resized import ResizedImageField

# Own's Libraries
from .utilities import Helper
from security.models import Profile


class Post(models.Model):

    STATUS = (
        ('PUB', 'PUBLICADO'),
        ('EDT', 'Editando'),
    )

    title = models.CharField("Titulo", max_length=120)
    image = ResizedImageField(
        "Imagen",
        upload_to=Helper.get_ImagePath_Post,
        quality=75,
        blank=True,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    content = models.TextField("Contenido", blank=True)

    status = models.CharField(
        "Estado",
        max_length=3,
        choices=STATUS,
        default="EDT"
    )
    created_by = models.ForeignKey(
        Profile,
        verbose_name="Creado por",
        related_name='post_created_by',
        null=True
    )
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(
        Profile,
        verbose_name="Actualizado por",
        related_name='post_updated_by',
        null=True
    )
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pubicación'
        verbose_name_plural = 'Publicaciones'
