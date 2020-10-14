import unidecode 
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
# Defines the status as published or draft
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post(models.Model):
    parent = models.ForeignKey("Post", blank= True, null= True, on_delete=models.SET("[deleted]"))
    title = models.CharField(max_length= 200)
    slug = models.SlugField(max_length= 500, unique= True, allow_unicode=True)
    # If user is deleted the default value for author becomes "[deleted]"
    author = models.ForeignKey(User, on_delete= models.SET("[deleted]"), null= True)
    description = models.CharField(max_length= 510)
    # RichTextField() is the field for ckeditor
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default= 0)
    created_on = models.DateTimeField(auto_now= True)
    updated_on = models.DateTimeField(auto_now= True)
    comments_enabled = models.BooleanField(default=True)

    class Meta:
        # The newly made post will be visible at the top
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        # creates a slug for the post on calling the save command
        now = datetime.now()
        self.slug = "%s_%s" %(slugify(unidecode.unidecode(self.title)),now.strftime("%m_%d_%Y_%H_%M_%S"))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
