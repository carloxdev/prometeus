# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recruited_date = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENEROS, max_length=144, null=True, blank=True)
    job_title = models.CharField(max_length=144, null=True, blank=True)
    department = models.CharField(max_length=144, null=True, blank=True)
    phone = models.CharField(max_length=144, null=True, blank=True)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
