# -*- coding: utf-8 -*-

# Librerias Python
import urllib


class Helper(object):

    @classmethod
    def get_Url_With_Querystring(self, path, **kwargs):
        return path + '?' + urllib.urlencode(kwargs)
