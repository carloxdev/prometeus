# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import Form
from django.forms import ValidationError

from django.forms import CharField

from django.forms import TextInput
from django.forms import PasswordInput

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


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


class PasswordResetRequestForm(PasswordResetForm):

    email = CharField(
        label='No. Empleado',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )

    def clean_email(self):
        username = self.cleaned_data["email"]

        try:
            active_user = User.objects.get(
                username__iexact=username,
                is_active=True,
            )

        except Exception as e:
            raise ValidationError(
                "No se encontro un Empleado con el numero %s" % (username)
            )

        if active_user.has_usable_password() is False:
            raise ValidationError(
                "El empleado con el numero %s no tiene una contraseña valida" % (username)
            )

        return active_user

    def save(self, domain_override=None,
             subject_template_name='password_reset/subject.txt',
             email_template_name='password_reset/email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """Generate a one-use only link for resetting password and sends to the user."""
        user = self.cleaned_data["email"]

        email = user.email
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override

        context = {
            'email': email,
            'domain': domain,
            'site_name': site_name,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': token_generator.make_token(user),
            'protocol': 'https' if use_https else 'http',
        }

        if extra_email_context is not None:
            context.update(extra_email_context)
        self.send_mail(
            subject_template_name, email_template_name, context, from_email,
            email, html_email_template_name=html_email_template_name,
        )

        return user


class PasswordResetConfirmForm(AdminPasswordChangeForm):
    password1 = CharField(
        label='Nueva contraseña',
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('password1', 'password2', )
