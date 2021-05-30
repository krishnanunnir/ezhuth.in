from datetime import datetime, timezone

from django import template

from feed.models import Like, Post

register = template.Library()


@register.filter(name="full_name")
def return_full_name(user):
    val = user.first_name + " " + user.last_name
    if val == " ":
        val = user.email
    return val
