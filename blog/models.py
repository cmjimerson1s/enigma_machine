from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    blog_image = CloudinaryField('image', default='placeholder')
    blog_blurb = models.TextField(blank=True)
    blog_content = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)
    meta_tags = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.blog_title