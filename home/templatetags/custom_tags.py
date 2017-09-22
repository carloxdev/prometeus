
# Python's Libraries
import os

# Django's Libraries
from django import template

register = template.Library()


@register.inclusion_tag('tags/message.html', takes_context=False)
def tag_message(_type, _text):
    """Show a message for the user.

        The type of message could be:
            - danger
            - success
            - primary
            - warning
    """
    contexto = {
        'type': _type,
        'text': _text
    }
    return contexto
