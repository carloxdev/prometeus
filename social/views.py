# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
# from django.shortcuts import render

# Third-party Libraries
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

# Own's Libraries
from .business import CommentBusiness


class CommentAddAPI(views.APIView):

    def post(self, request, format=None):

        try:
            obj = CommentBusiness.add(
                request.data['comment'],
                request.data['object_type'],
                request.data['object_id'],
                request.user.profile
            )

            lista = {
                'fecha': obj.created_date,
                'contenido': obj.content
            }
        except Exception as error:
            return Response(
                {'detail': str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            lista,
            status=status.HTTP_200_OK
        )
