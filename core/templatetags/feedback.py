# Django's Libraries
from django import template

register = template.Library()


@register.inclusion_tag('tags/feedback/message.html', takes_context=False)
def tag_message(_type, _text):
    """Show a message for the user.

        The type of message could be:
        - danger
        - success
        - primary
        - warning
    """
    context = {
        'type': _type,
        'text': _text
    }
    return context


@register.inclusion_tag('tags/feedback/messages.html', takes_context=False)
def tag_messages(_messages):
    context = {
        'messages': _messages,
    }
    return context
