# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.shortcuts import render
from django.shortcuts import redirect

# Own's Libraries
from security.mixins import GroupLoginRequiredMixin
from .business import PostBusiness

from .forms import PostAddForm
from .forms import PostEditForm


class PostList(GroupLoginRequiredMixin, View):
    template_name = 'post/list.html'
    group = ['NOTICIAS_ADM', ]

    def get(self, _request):
        query = _request.GET.get('q')
        posts = PostBusiness.get_FilterBy(query)
        posts_paginated = PostBusiness.get_Paginated(posts, _request.GET.get('page'))

        context = {
            'records': posts_paginated
        }

        return render(_request, self.template_name, context)


class PostAdd(GroupLoginRequiredMixin, View):
    template_name = 'post/add.html'
    group = ['NOTICIAS_ADM', ]

    def get(self, _request):
        form = PostAddForm()
        context = {
            'form': form
        }
        return render(_request, self.template_name, context)

    def post(self, _request):
        form = PostAddForm(_request.POST, _request.FILES)

        if form.is_valid():
            post = form.save(commit=False)

            post.created_by = _request.user.profile
            post.updated_by = _request.user.profile

            post.save()

            return redirect(
                reverse('editorial:post_edit', kwargs={'_pk': post.pk})
            )

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


class PostEdit(GroupLoginRequiredMixin, View):

    template_name = 'post/edit.html'
    group = ['NOTICIAS_ADM', ]

    def get(self, _request, _pk):

        form = PostEditForm(
            instance=PostBusiness.get(_pk)
        )

        context = {
            'form': form
        }

        return render(_request, self.template_name, context)

    def post(self, _request, _pk):

        form = PostEditForm(
            _request.POST,
            _request.FILES,
            instance=PostBusiness.get(_pk)
        )

        if form.is_valid():
            post = form.save(commit=False)
            post.updated_by = _request.user.profile
            post.save()

            messages.success(_request, "La Noticia fue actualizada correctamente")

        context = {
            'form': form
        }
        return render(_request, self.template_name, context)


class PostView(View):

    template_name = 'post/view.html'

    def get(self, _request, _pk):
        post = PostBusiness.get(_pk)
        last_post = PostBusiness.get_Last(post)

        context = {
            'record': post,
            'other_records': last_post
        }

        return render(_request, self.template_name, context)
