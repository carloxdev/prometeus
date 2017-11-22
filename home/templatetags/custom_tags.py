# Django's Libraries
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='filter_has_group')
def filter_has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


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


@register.inclusion_tag('tags/file.html', takes_context=False)
def tag_file(_file, _form):
    name = ""
    url = ""

    if _form.instance.file:
        name = _form.instance.file.name
        url = _form.instance.file.url

    context = {
        'file': _file,
        'name': name,
        'url': url
    }
    return context


@register.inclusion_tag('tags/dates.html', takes_context=False)
def tag_dates(_label_name, _is_optional, _field1, _field2):

    context = {
        'is_optional': _is_optional,
        'label_name': _label_name,
        'field1': _field1,
        'field2': _field2,
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


@register.inclusion_tag('tags/image_nopreview.html', takes_context=False)
def tag_image_nopreview(_field):

    context = {
        'field': _field
    }
    return context


@register.inclusion_tag('tags/form_errors.html', takes_context=False)
def tag_form_errors(_form):

    context = {
        'form': _form,
    }
    return context
