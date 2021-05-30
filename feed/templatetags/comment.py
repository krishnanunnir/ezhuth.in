from datetime import datetime, timezone

from django import template

from feed.models import Like, Post

register = template.Library()


@register.filter(name="comment_count")
def comment_count(post):
    return post.comment.count()
