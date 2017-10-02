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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_superuser',

        'recruited_date',
        'birth_date',
        'gender',
        'job_title',
        'department',
        'phone',
        'address',
    )
    list_select_related = ('profile', )

    def recruited_date(self, instance):
        return instance.profile.recruited_date

    def birth_date(self, instance):
        return instance.profile.birth_date

    def gender(self, instance):
        return instance.profile.gender

    def job_title(self, instance):
        return instance.profile.job_title

    def department(self, instance):
        return instance.profile.department

    def phone(self, instance):
        return instance.profile.phone

    def address(self, instance):
        return instance.profile.address

    # get_recruited_date.short_recruited_date = "Contratacion"
    # get_birth_date.short_birth_date = "Cumpleaños"
    # get_gender.short_gender = "Genero"
    # get_job_title.short_job_title = "Puesto"
    # get_department.short_department = "Departamento"
    # get_phone.short_phone = "Telefono"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class ProfileResource(resources.ModelResource):

    user_username = fields.Field(

        attribute="user",
        widget=ForeignKeyWidget(User, 'username')
    )

    user_first_name = fields.Field(

        attribute="user",
        widget=ForeignKeyWidget(User, 'first_name')
    )

    user_last_name = fields.Field(

        attribute="user",
        widget=ForeignKeyWidget(User, 'last_name')
    )

    user_email = fields.Field(

        attribute="user",
        widget=ForeignKeyWidget(User, 'email')
    )

    user_is_active = fields.Field(

        attribute="user",
        widget=ForeignKeyWidget(User, 'is_active')
    )

    class Meta:
        model = Profile
        exclude = ('id', )
        # skip_unchanged = True
        fields = (
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_email',
            'user_is_active',
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
        )
        import_id_fields = ['user_username', ]
        export_order = (
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_email',
            'user_is_active',
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
admin.site.register(User, CustomUserAdmin)
