from datetime import datetime, timezone

from django import template

from feed.models import Like, Post

register = template.Library()
