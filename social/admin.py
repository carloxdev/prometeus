# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import Comment

admin.site.register(Comment)
