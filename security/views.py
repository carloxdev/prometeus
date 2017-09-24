# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

from django.views.generic.base import View

# Own's Libraries
from .forms import LoginForm
from .forms import PasswordResetRequestForm
from .forms import PasswordResetConfirmForm


class Login(View):

    template_name = 'login.html'

    def get(self, _request):

        if _request.user.is_authenticated():
            return redirect(reverse('home:index'))

        else:
            formulario = LoginForm()

            contexto = {
                'form': formulario
            }

            return render(_request, self.template_name, contexto)

    def post(self, _request):

        formulario = LoginForm(_request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            cuenta = datos.get('username')
            contrasena = datos.get('password')

            user = authenticate(_request, username=cuenta, password=contrasena)

            if user is not None:
                login(_request, user)
                return redirect(reverse('home:index'))
            else:
                messages.error(
                    _request,
                    "Cuenta usuario o contraseña no valida"
                )

        context = {
            'form': formulario
        }

        return render(_request, self.template_name, context)


class PasswordResetRequest(View):

    template_name = "password_reset/request.html"

    def get(self, _request):

        formulario = PasswordResetRequestForm()

        contexto = {
            'form': formulario
        }

        return render(_request, self.template_name, contexto)

    def post(self, _request):

        formulario = PasswordResetRequestForm(_request.POST)

        if formulario.is_valid():

            formulario.save(
                use_https=_request.is_secure(),
                request=_request
            )

            messages.success(
                _request,
                "Se envio correo con instrucciones para cambiar su contraseña"
            )

        contexto = {
            'form': formulario
        }

        return render(_request, self.template_name, contexto)


class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm
    template_name = 'password_reset/confirm.html'
    success_url = reverse_lazy('security:password_reset_complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'password_reset/complete.html'


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
    template_name = "user_list.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class UserAdd(View):
    template_name = "user_add.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class UserAddSuccess(View):
    template_name = "user_add_success.html"

    def get(self, _request):
        return render(_request, self.template_name, {})


class UserEdit(View):
    template_name = "user_edit.html"

    def get(self, _request, _pk):
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
