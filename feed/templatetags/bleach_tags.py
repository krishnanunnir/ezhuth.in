import bleach
from django import template
from django.utils.safestring import mark_safe

allowed_tags = [
    "a",
    "abbr",
    "acronym",
    "b",
    "blockquote",
    "code",
    "em",
    "i",
    "li",
    "ol",
    "pre",
    "div",
    "del",
    "h1",
    "br",
    "p",
    "span",
    "strong",
    "ul",
    "img",
    "h2",
]
allowed_attributes = {
    "a": ["href", "title"],
    "abbr": ["title"],
    "acronym": ["title"],
    "img": ["src", "alt", "width", "height"],
}

register = template.Library()


@register.filter(name="bleach")
def bleach_value(value):
    if value is None:
        return None
    bleached_value = bleach.clean(
        value, tags=allowed_tags, attributes=allowed_attributes
    )
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
