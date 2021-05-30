from django.contrib import admin

from feed.models import Comment, Like, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
