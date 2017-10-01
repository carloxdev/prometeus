
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
    context = {
        'type': _type,
        'text': _text
    }
    return context


@register.inclusion_tag('tags/field.html', takes_context=False)
def tag_field(_field):

    context = {
        'field': _field,
    }
    return context


@register.inclusion_tag('tags/radio.html', takes_context=False)
def tag_radio(_field):

    context = {
        'field': _field,
    }
    return context


@register.inclusion_tag('tags/image.html', takes_context=False)
def tag_image(_field, _object):

    context = {
        'field': _field,
        'object': _object
    }
    return context


@register.inclusion_tag('tags/form_errors.html', takes_context=False)
def tag_form_errors(_form):

    context = {
        'form': _form,
    }
    return context
