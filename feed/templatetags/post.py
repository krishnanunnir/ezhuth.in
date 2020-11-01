from django import template
from datetime import datetime, timezone
from feed.models import Post, Like
register = template.Library()

@register.filter(name="post_description")
def comment_count(post):
    
    return post.content[0:30]