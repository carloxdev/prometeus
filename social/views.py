# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
# from django.shortcuts import render

# Third-party Libraries
from rest_framework.views import APIView
from rest_framework.response import Response

# Own's Libraries
from .models import Comment


class CommentAddAPI(APIView):

    def post(self, request, format=None):
        return Response("OK")
