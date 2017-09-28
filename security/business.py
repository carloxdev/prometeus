# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Own's Libraries
from .models import Profile


class UserBusiness(object):

    @classmethod
    def get(self, _pk):
        user = get_object_or_404(User, pk=_pk)
        return user

    @classmethod
    def get_Profile(self, _pk):
        profile = get_object_or_404(Profile, pk=_pk)
        return profile
