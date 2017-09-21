# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import Form

from django.forms import CharField

from django.forms import TextInput
from django.forms import PasswordInput


class LoginForm(Form):

    username = CharField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'cuenta'
        })
    )

    password = CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'contraseña'
        })
    )
