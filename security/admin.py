# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Third-party Libraries
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
# from import_export.widgets import DateWidget

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
        skip_unchanged = True
        import_id_fields = ['username', ]
        export_order = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    inlines = (ProfileInline, )
    resource_class = UserResource
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',

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

    username = fields.Field(
        column_name='username',
        attribute="user",
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Profile
        skip_unchanged = True
        exclude = ('id', )
        fields = (
            'username',
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
        )
        import_id_fields = ['username']
        widgets = {
            'recruited_date': {'format': '%d/%m/%Y'},
            'birth_date': {'format': '%d/%m/%Y'},
        }
        export_order = (
            'username',
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
        )


# @admin.register(Profile)
# class AdminProfile(ImportExportModelAdmin):
#     resource_class = ProfileResource
#     list_display = (
#         'user',
#         'recruited_date',
#         'birth_date',
#         'gender',
#         'job_title',
#         'department',
#         'phone',
#         'address',
#     )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
