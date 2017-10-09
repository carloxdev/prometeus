# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals
import os

# Django's Libraries
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.conf import settings

# Own's Libraries
from home.utilities import Helper
from security.models import Profile


def get_ImagePath_Post(_instance, _filename):

    if (_instance):
        upload_dir = os.path.join(
            'images',
            'post',
            str(_instance.pk)
        )

        extension = os.path.splitext(_filename)[1]

        filename = "%s_image%s" % (_instance.pk, extension)

    return os.path.join(upload_dir, filename)


class Post(models.Model):

    STATUS = (
        ('PUB', 'PUBLICADO'),
        ('EDT', 'Editando'),
    )

    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=get_ImagePath_Post,
        blank=True,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    content = models.TextField(blank=True)

    status = models.CharField(max_length=3, choices=STATUS, default="EDT")
    created_by = models.ForeignKey(Profile, related_name='post_created_by', null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(Profile, related_name='post_updated_by', null=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Post)
def delete_Photo(sender, instance, using, **kwargs):
    file_path = settings.BASE_DIR + "/media/" + "%s" % (instance.image)
    if os.path.isfile(file_path):
        os.remove(file_path)
