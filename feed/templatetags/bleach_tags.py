import bleach

from django import template
from django.utils.safestring import mark_safe

import bleach
allowed_tags =['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'pre' ,'div','del','h1','br']

register = template.Library()


@register.filter(name='bleach')
def bleach_value(value):
    if value is None:
        return None
    bleached_value = bleach.clean(value, tags= allowed_tags)
    return mark_safe(bleached_value)


@register.filter
def bleach_linkify(value):
    """
    Convert URL-like strings in an HTML fragment to links

    This function converts strings that look like URLs, domain names and email
    addresses in text that may be an HTML fragment to links, while preserving:

        1. links already in the string
        2. urls found in attributes
        3. email addresses
    """
    if value is None:
        return None

    return bleach.linkify(value, parse_email=True)
