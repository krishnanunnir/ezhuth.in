from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Defines the status as published or draft
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length= 255, unique= True)
    # If user is deleted the default value for author becomes "[deleted]"
    author = models.ForeignKey(User, on_delete= models.SET("[deleted]"), null= True)
    description = models.CharField(max_length= 510,default=  "No description provided")
    # RichTextField() is the field for ckeditor
    content = RichTextField()
    status = models.IntegerField(choices= STATUS, default= 0)
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        # The newly made post will be visible at the top
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        # creates a slug for the post on calling the save command
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.SET("[deleted]"), null= True)
    content = RichTextField()
    post = models.ForeignKey(Post, on_delete= models.CASCADE, null= True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.content + ".... " 