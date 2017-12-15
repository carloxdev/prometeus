# -*- coding: utf-8 -*-

# Python's Libraries
import os


def get_ImagePath_Post(_instance, _filename):

    if (_instance):
        upload_dir = os.path.join(
            'images',
            'posts'
        )
    return os.path.join(upload_dir, _filename)
