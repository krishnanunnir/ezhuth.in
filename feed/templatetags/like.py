from django import template
from datetime import datetime, timezone
from feed.models import Post, Like
register = template.Library()

@register.filter(name="like_count")
def return_like_count(post):
    liked_object = Like.objects.get(like_for=post)
    return liked_object.users.count()

@register.simple_tag(takes_context=True)
def liked_by_user(context, post):
    user = context["user"]
    liked_object = Like.objects.get(like_for=post)
    if user in liked_object.users.all():
        return True
    else:
        return False
