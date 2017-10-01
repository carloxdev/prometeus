# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
