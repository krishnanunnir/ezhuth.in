from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, register_converter

from feed import views

from . import converters

app_name = "feed"
urlpatterns = [
    path("read/", views.view_all, name="view_all"),
    path("feed/", views.view_feed, name="view_feed"),
    path("add/", views.add_post, name="add_post"),
    path("view/<slug:post_slug>", views.view_post, name="view_post"),
    path("drafts/", views.view_drafts, name="view_drafts"),
    path("edit/<slug:post_slug>", views.edit_post, name="edit_post"),
    path("like/<slug:post_slug>", views.like_post, name="like_post"),
    path("like/comment/<int:id>", views.like_comment, name="like_comment"),
    path("user/<uuid:username>", views.view_user, name="view_user"),
    path("delete/<slug:post_slug>", views.delete_post, name="delete_post"),
    path("preview/<slug:post_slug>", views.preview_post, name="preview_post"),
    path("uploadfile/", views.handle_image, name="handle_image"),
    path("writer/", views.write, name="write"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
