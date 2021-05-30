from django import template
from datetime import datetime, timezone
from django.utils.translation import gettext as _

register = template.Library()

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now(timezone.utc)
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return _("Just now")
        if second_diff < 60:
            return str(second_diff) + _(" seconds ago")
        if second_diff < 120:
            return _("A minute ago")
        if second_diff < 3600:
            return str(second_diff // 60) + _(" minutes ago")
        if second_diff < 7200:
            return _("An hour ago")
        if second_diff < 86400:
            return str(second_diff // 3600) + _(" hours ago")
    if day_diff == 1:
        return _("Yesterday")
    if day_diff < 7:
        return str(day_diff) + _(" days ago")
    if day_diff < 31:
        return str(day_diff // 7) + _(" weeks ago")
    if day_diff < 365:
        return str(day_diff // 30) + _(" months ago")
    return str(day_diff // 365) + _(" years ago")


register.filter("pretty_date", pretty_date)