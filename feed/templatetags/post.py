from django import template
from datetime import datetime, timezone
from feed.models import Post, Like
register = template.Library()

