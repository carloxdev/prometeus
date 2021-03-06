# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import get_object_or_404

from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Own's Libraries
from .models import Post


class PostBusiness(object):

    @classmethod
    def get(self, _pk):
        post = get_object_or_404(Post, pk=_pk)
        return post

    @classmethod
    def get_FilterBy(self, _value):
        if _value:
            post = Post.objects.filter(
                Q(title__icontains=_value) |
                Q(content__icontains=_value)
            ).order_by("-created_date")
        else:
            post = Post.objects.all().order_by("-created_date")

        return post

    @classmethod
    def get_Published(self):
        posts = Post.objects.filter(status="PUB").order_by("-created_date")
        return posts

    @classmethod
    def get_Paginated(self, _posts, _current_page):
        paginator = Paginator(_posts, 20)
        current_pagina = _current_page

        try:
            _posts = paginator.page(current_pagina)
        except PageNotAnInteger:
            _posts = paginator.page(1)
        except EmptyPage:
            _posts = paginator.page(paginator.num_page)

        return _posts

    @classmethod
    def get_Last(self, _post):
        posts = Post.objects.all().exclude(pk=_post.pk).order_by("-created_date")[:10]
        return posts
