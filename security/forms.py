# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import Form
from django.forms import ModelForm
from django.forms import ValidationError

from django.forms import CharField
from django.forms import DateField
from django.forms import EmailField
from django.forms import ChoiceField

from django.forms import TextInput
from django.forms import DateInput
from django.forms import PasswordInput
from django.forms import EmailInput
from django.forms import RadioSelect
from django.forms import ClearableFileInput

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe


# Own's Libraries
from .models import Profile


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
            attrs={'class': 'form-control'}
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
             subject_template_name='password/subject.txt',
             email_template_name='password/email.html',
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


class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'username': 'Clave',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = "Longitud máxima 150 caracteres alfanuméricos. Letras, dígitos y @/./+/-/_ únicamente."
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        self.fields['password1'].help_text = mark_safe("<ul><li>La contraseña no puede ser similar a su otra información personal.</li><li>La contraseña debe contener al menos 8 caracteres.</li><li>La contraseña no puede ser una contraseña común.</li><li>La contraseña no puede ser enteramente numérica.</li></ul>")
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['password2'].help_text = "Para verificar, introduzca la misma contraseña que introdujo antes."
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
        )

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'username': 'Clave',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = "Longitud máxima 150 caracteres alfanuméricos. Letras, dígitos y @/./+/-/_ únicamente."
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True


class UserProfileForm(ModelForm):

    recruited_date = DateField(
        required=False,
        label="Contratacion",
        input_formats=[
            "%d/%m/%Y",
        ],
        widget=DateInput(
            attrs={'class': 'form-control'}
        )
    )

    birth_date = DateField(
        required=False,
        label="Fecha Nacimiento",
        input_formats=[
            "%d/%m/%Y",
        ],
        widget=DateInput(
            attrs={'class': 'form-control'}
        )
    )

    gender = ChoiceField(
        required=False,
        label="Genero",
        choices=Profile.GENEROS,
        widget=RadioSelect()
    )

    class Meta:
        model = Profile
        fields = (
            'recruited_date',
            'birth_date',
            'gender',
            'job_title',
            'department',
            'phone',
            'address',
            'photo',
        )

        widgets = {
            'job_title': TextInput(attrs={'class': 'form-control'}),
            'department': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': "Seleccionar Imagen",
                'data-iconName': "glyphicon glyphicon-picture"
            })
        }

        labels = {
            'job_title': 'Puesto',
            'department': 'Departamento',
            'phone': 'Telefono',
            'address': 'Direccion',
            'photo': 'Foto',
        }


class UserPasswordForm(AdminPasswordChangeForm):
    password1 = CharField(
        label='Nueva contraseña',
        help_text=mark_safe("<ul><li>La contraseña no puede ser similar a su otra información personal.</li><li>La contraseña debe contener al menos 8 caracteres.</li><li>La contraseña no puede ser una contraseña común.</li><li>La contraseña no puede ser enteramente numérica.</li></ul>"),
        widget=PasswordInput(
            attrs={'class': 'form-control input-xs'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        help_text="Para verificar, introduzca la misma contraseña que introdujo antes.",
        widget=PasswordInput(
            attrs={'class': 'form-control input-xs'}
        )
    )


class ProfilePasswordForm(PasswordChangeForm):

    old_password = CharField(
        label='Contraseña Actual',
        widget=PasswordInput(
            attrs={'class': 'form-control input-xs', 'autofocus': True}
        )
    )

    new_password1 = CharField(
        label='Nueva contraseña',
        help_text=mark_safe("<ul><li>La contraseña no puede ser similar a su otra información personal.</li><li>La contraseña debe contener al menos 8 caracteres.</li><li>La contraseña no puede ser una contraseña común.</li><li>La contraseña no puede ser enteramente numérica.</li></ul>"),
        widget=PasswordInput(
            attrs={'class': 'form-control input-xs'}
        )
    )
    new_password2 = CharField(
        label='Confirmar contraseña',
        help_text="Para verificar, introduzca la misma contraseña que introdujo antes.",
        widget=PasswordInput(
            attrs={'class': 'form-control input-xs'}
        )
    )
