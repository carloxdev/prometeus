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
    content = models.TextField()
    created_by = models.ForeignKey(
        Profile,
        related_name='comments_created_by',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
