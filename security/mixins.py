# -*- coding: utf-8 -*-

# Django's Libraries
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User


class GroupLoginRequiredMixin(object):
    """
    View mixin which verifies that the user has authenticated.

    If group is specified by the parent class, then user must be member of that group (as set in django admin)
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
                user = User.objects.get(username=request.user.username)

                # if parent class has group attribute
                if user.is_superuser is False:
                    self.validate_Groups(user)
        else:
            return redirect(reverse('security:login'))
        return super(GroupLoginRequiredMixin, self).dispatch(request, *args, **kwargs)

    def validate_Groups(self, _user):
        if hasattr(self, 'group'):
            grps = _user.groups.filter(name__in=self.group)
            if not grps:
                raise PermissionDenied("No se tienen los permisos para entrar a esta sección")
