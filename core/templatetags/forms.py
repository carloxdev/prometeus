# Python's Libraries
import os

# Django's Libraries
from django import template

register = template.Library()


@register.inclusion_tag('tags/forms/form_errors.html', takes_context=False)
def tag_form_errors(_form):

    context = {
        'form': _form,
    }
    return context


@register.inclusion_tag('tags/forms/field.html', takes_context=False)
def tag_field(_field):

    context = {
        'field': _field,
    }
    return context


@register.inclusion_tag('tags/forms/dates.html', takes_context=False)
def tag_dates(_label_name, _is_optional, _field1, _field2):
    context = {
        'is_optional': _is_optional,
        'label_name': _label_name,
        'field1': _field1,
        'field2': _field2,
    }
    return context


@register.inclusion_tag('tags/forms/date.html', takes_context=False)
def tag_date(_label_name, _is_optional, _field):
    context = {
        'is_optional': _is_optional,
        'label_name': _label_name,
        'field': _field
    }
    return context


@register.inclusion_tag('tags/forms/radio.html', takes_context=False)
def tag_radio(_field):

    context = {
        'field': _field,
    }
    return context


@register.inclusion_tag('tags/forms/image.html',
                        takes_context=False)
def tag_image(_field, _object):

    context = {
        'field': _field,
        'object': _object
    }
    return context


@register.inclusion_tag('tags/forms/image_nopreview.html',
                        takes_context=False)
def tag_image_nopreview(_field):

    context = {
        'field': _field
    }
    return context


@register.filter
def get_filename(value):
    return os.path.basename(value.file.name)


@register.inclusion_tag('tags/forms/file.html', takes_context=False)
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
