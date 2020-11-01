from django import template
from datetime import datetime, timezone
from feed.models import Post, Like
register = template.Library()

@register.filter(name="comment_count")
def comment_count(post):
    return post.comment.count()