# -*- coding: utf-8 -*-

# Python's Libraries
import urllib

# Django's Libraries
from django.core.exceptions import ValidationError


class Helper(object):

    @classmethod
    def get_Url_With_Querystring(self, path, **kwargs):
        return path + '?' + urllib.urlencode(kwargs)

    @classmethod
    def validate_Img_Extension(self, obj):
        if (not obj.name.endswith('.png') and
            not obj.name.endswith('.jpeg') and
            not obj.name.endswith('.jpg') and
            not obj.name.endswith('.PNG') and
            not obj.name.endswith('.JPEG') and
                not obj.name.endswith('.JPG')):

            raise ValidationError("Solo se permiten archivos con extensión: .jpg, .jpeg, .png")

    @classmethod
    def validate_Size(self, obj):
        filesize = obj.file.size
        megabyte_limit = 10.0
        bits_limit = megabyte_limit * 1024 * 1024
        if filesize > bits_limit:
            raise ValidationError("Tamaño máximo permitido %sMB" %
                                  str(megabyte_limit))

    @classmethod
    def get_ImagePath_Profile(_instance, _filename):

        if (_instance):
            upload_dir = os.path.join(
                'images',
                'profile',
                _instance.pk
            )

        return os.path.join(upload_dir, _filename)

    @classmethod
    def get_ImagePath_Post(_instance, _filename):

        if (_instance):
            upload_dir = os.path.join(
                'images',
                'post',
                _instance.pk
            )

        return os.path.join(upload_dir, _filename)
