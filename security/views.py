# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

from django.views.generic import ListView
from django.views.generic.base import View

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.db.models import Q

# Own's Libraries
from home.utilities import Helper

from .business import UserBusiness

from .forms import LoginForm
from .forms import PasswordResetRequestForm
from .forms import PasswordResetConfirmForm
from .forms import UserAddForm
from .forms import UserEditForm
from .forms import ProfileForm


class Login(View):

    template_name = 'login.html'

    def get(self, _request):

        if _request.user.is_authenticated():
            return redirect(reverse('home:index'))

        else:
            form = LoginForm()

            context = {
                'form': form
            }

            return render(_request, self.template_name, context)

    def post(self, _request):

        form = LoginForm(_request.POST)

        if form.is_valid():
            data = form.cleaned_data
            account = data.get('username')
            password = data.get('password')

            user = authenticate(_request, username=account, password=password)

            if user is not None:
                login(_request, user)
                return redirect(reverse('home:index'))
            else:
                messages.error(
                    _request,
                    "Cuenta de usuario o contraseña no valida"
                )

        context = {
            'form': form
        }

        return render(_request, self.template_name, context)


class PasswordResetRequest(View):

    template_name = "password_reset/request.html"

    def get(self, _request):

        form = PasswordResetRequestForm()

        context = {
            'form': form
        }

        return render(_request, self.template_name, context)

    def post(self, _request):

        form = PasswordResetRequestForm(_request.POST)

        if form.is_valid():

            user = form.save(
                use_https=_request.is_secure(),
                request=_request
            )

            return redirect(reverse(
                'security:password_reset_message',
                kwargs={'_pk': user.pk}
            ))

        context = {
            'form': form
        }

        return render(_request, self.template_name, context)


class PasswordResetMessage(View):

    template_name = "password_reset/message.html"

    def get(self, _request, _pk):

        user = User.objects.get(pk=_pk)

        context = {
            'email': user.email
        }

        return render(_request, self.template_name, context)


class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm
    template_name = 'password_reset/confirm.html'
    success_url = reverse_lazy('security:password_reset_done')


class PasswordResetDone(PasswordResetCompleteView):
    template_name = 'password_reset/done.html'


class Profile(View):
    template_name = "profile.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class ProfilePassword(View):
    template_name = "profile_password.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class ProfilePasswordSuccess(View):
    template_name = "profile_password_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class UserList(View):
    template_name = "user/list.html"

    def get(self, _request):

        query = _request.GET.get('q')
        if query:
            users = User.objects.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            ).order_by("-date_joined")
        else:
            users = User.objects.all().order_by("-date_joined")

        paginator = Paginator(users, 10)
        current_pagina = _request.GET.get('page')

        try:
            users = paginator.page(current_pagina)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_page)

        context = {
            'users': users
        }

        return render(_request, self.template_name, context)


class UserAdd(View):
    template_name = "user/add.html"

    def get(self, _request):
        form = UserAddForm()
        context = {
            'form': form
        }
        return render(_request, self.template_name, context)

    def post(self, _request):
        form = UserAddForm(_request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(Helper.get_Url_With_Querystring(
                reverse('security:user_edit', kwargs={'_pk': user.pk}),
                new=True
            ))

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


class UserEdit(View):
    template_name = "user/edit.html"

    def get(self, _request, _pk):
        # print _request.GET['new']
        form = UserEditForm(instance=UserBusiness.get(_pk))
        context = {
            'form': form
        }
        return render(_request, self.template_name, context)

    def post(self, _request, _pk):
        form = UserEditForm(
                _request.POST,
                instance=UserBusiness.get(_pk)
            )

        if form.is_valid():
            form.save()
            messages.success(_request, "El usuario fue actualizado correctamente")

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


class UserEmployee(View):
    template_name = "user/employee.html"

    def get(self, _request, _pk):
        form = ProfileForm(instance=UserBusiness.get_Profile(_pk))
        context = {
            'form': form
        }
        return render(_request, self.template_name, context)

    def post(self, _request, _pk):

        form = ProfileForm(
            _request.POST,
            instance=UserBusiness.get_Profile(_pk)
        )

        if form.is_valid():
            form.save()
            messages.success(_request, "La informacion de Empleado fue actualizada correctamente")

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


class UserAddSuccess(View):
    template_name = "user_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class UserPermissions(View):
    template_name = "user_permissions.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class UserPassword(View):
    template_name = "user_password.html"

    def get(self, _request, _pk):
        return render(_request, self.template_name, {})


class UserPasswordSuccess(View):
    template_name = "user_password_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})
