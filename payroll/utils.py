# -*- coding: utf-8 -*-

# Python's Libraries
import os


def get_FilePath_Voucher(_instance, _filename):

    if (_instance):
        upload_dir = os.path.join(
            'files',
            'vouchers',
        )
    return os.path.join(upload_dir, _filename)
