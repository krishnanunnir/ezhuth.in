from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from datetime import datetime
# Defines the status as published or draft
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post(models.Model):
    parent = models.ForeignKey("Post", blank= True, null= True, on_delete=models.SET("[deleted]"))
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length= 255, unique= True)
    # If user is deleted the default value for author becomes "[deleted]"
    author = models.ForeignKey(User, on_delete= models.SET("[deleted]"), null= True)
    description = models.CharField(max_length= 510,default=  "No description provided")
    # RichTextField() is the field for ckeditor
    content = HTMLField()
    status = models.IntegerField(choices= STATUS, default= 0)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    comments_enabled = models.BooleanField(default=True)

    class Meta:
        # The newly made post will be visible at the top
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        # creates a slug for the post on calling the save command
        now = datetime.now()
        self.created_on = now
        self.slug = "%s_%s" %(slugify(self.title),now.strftime("%m_%d_%Y_%H_%M_%S"))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
