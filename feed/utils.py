from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.views.decorators.http import require_GET, require_POST


def is_ajax(request):
    """
    This utility function is used, as `request.is_ajax()` is deprecated.

    This implements the previous functionality. Note that you need to
    attach this header manually if using fetch.
    """
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def paginate_posts(request, all_posts, post_per_page):
    paginator = Paginator(all_posts, per_page=post_per_page)
    page_num = int(request.GET.get("page", 1))
    if page_num > paginator.num_pages:
        raise Http404
    posts = paginator.page(page_num)
    return posts
