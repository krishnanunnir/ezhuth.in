from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post(models.Model):
    title = models.CharField(max_length= 255, unique= True)
    slug = models.SlugField(max_length= 255, unique= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default= 0)
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title;