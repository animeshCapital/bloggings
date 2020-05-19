from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class PostCategory(models.Model):
    slug = models.SlugField(null=True, unique=True)
    name = models.CharField(null=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    title = models.CharField(null=True, max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='post_image' ,null=True, blank=True)
    status = models.BooleanField(default=1, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    postcategory = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title 

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Post, self).delete(*args, **kwargs)
        storage.delete(path) 

class Like(models.Model):
    like =  models.BooleanField(default=0, null=True) 
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)           
    post = models.ManyToManyField(Post)
    date_created = models.DateTimeField(auto_now_add=True, null=True)           