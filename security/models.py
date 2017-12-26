# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Third-party Libraries
from django_resized import ResizedImageField

# Own's Libraries
from .utilities import Helper


class Profile(models.Model):

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recruited_date = models.DateField(
        "Fecha de Contratacion",
        null=True,
        blank=True
    )
    birth_date = models.DateField(
        "Fecha de Nacimiento",
        null=True,
        blank=True
    )
    gender = models.CharField(
        "Genero",
        choices=GENEROS, max_length=144, null=True, blank=True
    )
    job_title = models.CharField(
        "Puesto",
        max_length=144,
        null=True,
        blank=True
    )
    department = models.CharField(
        "Departamento",
        max_length=144,
        null=True,
        blank=True
    )
    phone = models.CharField("Telefono", max_length=144, null=True, blank=True)
    address = models.CharField(
        "Dirección",
        max_length=255,
        null=True,
        blank=True
    )
    photo = ResizedImageField(
        "Foto",
        upload_to=Helper.get_ImagePath_Profile,
        quality=75,
        blank=True,
        keep_meta=False,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    reset_password = models.BooleanField("Reset Contraseña", default=True)
    first_login = models.BooleanField("Primer Login", default=True)

    def __unicode__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
