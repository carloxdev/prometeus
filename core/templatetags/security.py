# Django's Libraries
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='check_has_group')
def check_has_group(user, group_name):
    """Validate is a user is in a group."""
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()
