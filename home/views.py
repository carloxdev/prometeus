# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.views.generic.base import View

from editorial.business import PostBusiness


class Index(View):
    template_name = "index.html"

    def get(self, _request):
        posts = PostBusiness.get_Published()
        posts_paginated = PostBusiness.get_Paginated(posts, _request.GET.get('page'))

        context = {
            'records': posts_paginated
        }

        return render(_request, self.template_name, context)
