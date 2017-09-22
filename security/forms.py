# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import Form

from django.forms import CharField

from django.forms import TextInput
from django.forms import PasswordInput

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
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


class CustomPasswordResetForm(PasswordResetForm):
    email = CharField(
        label='No. Empleado',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )

    def get_users(self, _username):
        """Given an _username, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = User.objects.filter(
            username__iexact=_username,
            is_active=True,
        )
        return (u for u in active_users if u.has_usable_password())

    def save(self, domain_override=None,
             subject_template_name='password_reset/subject.txt',
             email_template_name='password_reset/email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """Generate a one-use only link for resetting password and sends to the user."""
        username = self.cleaned_data["email"]

        for user in self.get_users(username):
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
