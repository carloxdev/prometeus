# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_by',
        'created_date',
        'updated_date',
        'updated_by',
    )
