# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Own's Libraries
from home.utilities import Helper
from security.models import Profile


class Post(models.Model):

    STATUS = (
        ('PUB', 'PUBLICADO'),
        ('EDT', 'Editando'),
    )

    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=Helper.get_ImagePath_Post,
        blank=True,
        validators=[
            Helper.validate_Img_Extension,
            Helper.validate_Size
        ]
    )
    content = models.TextField()

    status = models.CharField(max_length=3, choices=STATUS, default="EDT")
    created_by = models.ForeignKey(Profile, related_name='post_created_by', null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(Profile, related_name='post_updated_by', null=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
