# -*- coding: utf-8 -*-

# Python's Libraries
import urllib
import os

# Django's Libraries
from django.core.exceptions import ValidationError


class Helper(object):

    @classmethod
    def get_Url_With_Querystring(self, _path, **kwargs):
        return _path + '?' + urllib.urlencode(kwargs)

    @classmethod
    def validate_Img_Extension(self, _obj):
        if (not _obj.name.endswith('.png') and
            not _obj.name.endswith('.jpeg') and
            not _obj.name.endswith('.jpg') and
            not _obj.name.endswith('.PNG') and
            not _obj.name.endswith('.JPEG') and
                not _obj.name.endswith('.JPG')):

            raise ValidationError("Solo se permiten archivos con extensión: .jpg, .jpeg, .png")

    @classmethod
    def validate_Size(self, _obj):
        filesize = _obj.file.size
        megabyte_limit = 10.0
        bits_limit = megabyte_limit * 1024 * 1024
        if filesize > bits_limit:
            raise ValidationError("Tamaño máximo permitido %sMB" %
                                  str(megabyte_limit))

    # @classmethod
    # def get_ImagePath_Post(self, _instance, _filename):
    #
    #     if (_instance):
    #         upload_dir = os.path.join(
    #             'images',
    #             'post',
    #             str(_instance.pk)
    #         )
    #
    #     return os.path.join(upload_dir, _filename)

    # @classmethod
    # def get_ImagePath_Profile(self, _instance, _filename):
    #
    #     if (_instance):
    #         upload_dir = os.path.join(
    #             'images',
    #             'profile',
    #             str(_instance.pk)
    #         )
    #
    #     return os.path.join(upload_dir, _filename)
