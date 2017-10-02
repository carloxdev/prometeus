# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Import-Export
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Own's Libraries
from .models import Profile


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        exclude = ('id', )
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )
        import_id_fields = ['username']
        export_order = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    pass


class ProfileResource(resources.ModelResource):

    user_username = fields.Field(
        column_name='user_username',
        attribute="user",
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Profile
        skip_unchanged = True
        exclude = ('id', )
        fields = (
            'user_username',
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
        )
        import_id_fields = ['user_username']
        export_order = (
            'user_username',
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
        )


@admin.register(Profile)
class AdminProfile(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = (
        'user',
        'recruited_date',
        'birth_date',
        'gender',
        'job_title',
        'department',
        'phone',
        'address',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
