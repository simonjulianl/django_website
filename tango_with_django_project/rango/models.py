from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True, null = False)
    name_length = 128
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(blank = True, unique = True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 128)
    #class attribute 
    title_length = 128
    url = models.URLField(max_length = 200)
    url_length = 200
    views = models.IntegerField(default = 0)
    slug = models.SlugField(blank = True)
    last_visit = models.DateTimeField(default = datetime.now())
    first_visit = models.DateTimeField(default = datetime.now())
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,)

    #additional attribute
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __str__(self):
        return self.user.username
    
