from datetime import datetime, timezone

import unidecode
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

from authentication.models import User

# Defines the status as published or draft


STATUS = ((0, "Hidden"), (1, "Visible"), (2, "Home"))


class Tag(models.Model):
    owner = models.ForeignKey(
        User, related_name="user_owned_tags", on_delete=models.SET_NULL, null=True
    )
    tag_name = models.CharField(max_length=200)


class Like(models.Model):
    users = models.ManyToManyField(User, related_name="requirement_comment_likes")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("content_type", "object_id")


class Comment(models.Model):
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_on = models.DateTimeField(auto_now=True)
    like = GenericRelation(Like, related_query_name="like_for_comment")


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True)
    # If user is deleted the default value for author becomes "[deleted]"
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # RichTextField() is the field for ckeditor
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    comments_enabled = models.BooleanField(default=True)
    comment = GenericRelation(Comment)
    like = GenericRelation(Like, related_query_name="like_for_post")
    tag = models.ForeignKey(
        Tag, related_name="tag_posts", null=True, on_delete=models.SET_NULL
    )
    description = models.CharField(max_length=500, null=True, blank=True)
    header_image = models.ImageField(blank=True)

    class Meta:
        # The newly made post will be visible at the top
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        # creates a slug for the post on calling the save command
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/view/%s" % (self.slug)


class ImageTinymce(models.Model):
    image = models.ImageField()
