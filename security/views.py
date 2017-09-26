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
from .forms import LoginForm
from .forms import PasswordResetRequestForm
from .forms import PasswordResetConfirmForm
from .forms import UserAddForm


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
                    "Cuenta de usuario o contraseña no valida"
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

            user = formulario.save(
                use_https=_request.is_secure(),
                request=_request
            )

            return redirect(reverse(
                'security:password_reset_message',
                kwargs={'_pk': user.pk}
            ))

        contexto = {
            'form': formulario
        }

        return render(_request, self.template_name, contexto)


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

    def get(self, request):

        query = request.GET.get('q')
        if query:
            usuarios = User.objects.filter(
                Q(titulo__icontains=query) |
                Q(contenido__icontains=query)
            ).order_by("-date_joined")
        else:
            usuarios = User.objects.all().order_by("-date_joined")

        paginador = Paginator(usuarios, 10)
        pagina = request.GET.get('page')

        try:
            usuarios = paginador.page(pagina)
        except PageNotAnInteger:
            usuarios = paginador.page(1)
        except EmptyPage:
            usuarios = paginador.page(paginador.num_page)

        contexto = {
            'usuarios': usuarios
        }

        return render(request, self.template_name, contexto)


class UserAdd(View):
    template_name = "user/add.html"

    def get(self, _request):

        form = UserAddForm()

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


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
