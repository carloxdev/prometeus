# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals
import os

# Django's Libraries
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.db.models.signals import pre_save
from django.dispatch import receiver
# from django.conf import settings

# Third-party Libraries
from django_resized import ResizedImageField

# Own's Libraries
from home.utilities import Helper


def get_ImagePath_Profile(_instance, _filename):

    if (_instance):
        upload_dir = os.path.join(
            'images',
            'profile',
            str(_instance.pk)
        )

        extension = os.path.splitext(_filename)[1]

        filename = "%s_image%s" % (_instance.pk, extension)

    return os.path.join(upload_dir, filename)


class Profile(models.Model):

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recruited_date = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        choices=GENEROS, max_length=144, null=True, blank=True
    )
    job_title = models.CharField(max_length=144, null=True, blank=True)
    department = models.CharField(max_length=144, null=True, blank=True)
    phone = models.CharField(max_length=144, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = ResizedImageField(
        upload_to=get_ImagePath_Profile,
        quality=75,
        blank=True,
        keep_meta=False,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    reset_password = models.BooleanField(default=True)
    first_login = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
