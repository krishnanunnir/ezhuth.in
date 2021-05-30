from datetime import datetime, timezone

from django import template

from feed.models import Like, Post

register = template.Library()


@register.filter(name="post_like_count")
def return_post_like_count(post):
    liked_object = Like.objects.get(like_for_post=post)
    return liked_object.users.count()


@register.simple_tag(takes_context=True)
def post_liked_by_user(context, post):
    user = context["user"]
    liked_object = Like.objects.get(like_for_post=post)
    if user in liked_object.users.all():
        return True
    else:
        return False


@register.filter(name="comment_like_count")
def return_comment_like_count(comment):
    liked_object = Like.objects.get(like_for_comment=comment)
    return liked_object.users.count()


@register.simple_tag(takes_context=True)
def comment_liked_by_user(context, comment):
    user = context["user"]
    liked_object = Like.objects.get(like_for_comment=comment)
    if user in liked_object.users.all():
        return True
    else:
        return False
