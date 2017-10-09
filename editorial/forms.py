# -*- coding: utf-8 -*-

# Django's Libraries
from django.forms import Form
from django.forms import ModelForm
from django.forms import ValidationError

from django.forms import Select
from django.forms import TextInput
from django.forms import Textarea
from django.forms import ClearableFileInput

# Own's Libraries
from .models import Post


class PostAddForm(ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'content',
        )

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'image': ClearableFileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': "Seleccionar Imagen",
                'data-iconName': "glyphicon glyphicon-picture"
            }),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
        }

        labels = {
            'title': 'Titulo de la publicacion',
            'image': 'Portada',
            'content': 'Contenido',
        }


class PostEditForm(ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'content',
            'status',
        )

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'image': ClearableFileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': "Seleccionar Imagen",
                'data-iconName': "glyphicon glyphicon-picture"
            }),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            'status': Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Titulo de la publicacion',
            'image': 'Portada',
            'content': 'Contenido',
            'status': 'Estado',
        }
