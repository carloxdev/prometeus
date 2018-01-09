# Django's Libraries
from django import template


register = template.Library()


@register.inclusion_tag('tags/comments.html', takes_context=False)
def tag_comments(_instance):
    context = {
        'instance': _instance
    }
    return context
