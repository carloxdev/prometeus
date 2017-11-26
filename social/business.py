# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib.contenttypes.models import ContentType

# Own's Libraries
from .models import Comment


class CommentBusiness(object):

    @classmethod
    def get(self, _object_type, _object_id):
        content_type = ContentType.objects.get_for_model(_object_type)
        records = Comment.objects.filter(
            content_type=content_type,
            object_id=_object_id
        ).order_by('-created_date')
        return records
