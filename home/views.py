# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic.base import View
from django.core.urlresolvers import reverse

# Own's Libraries
from editorial.business import PostBusiness


class LandingView(View):
    template_name = "landing.html"

    def get(self, _request):

        if _request.user.is_authenticated():
            return redirect(reverse('security:index'))
        else:
            posts = PostBusiness.get_Published()
            posts_paginated = PostBusiness.get_Paginated(
                posts,
                _request.GET.get('page')
            )

        context = {
            'records': posts_paginated
        }

        return render(_request, self.template_name, context)
