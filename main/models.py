from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.sitemaps import ping_google
from django.conf import settings

from ckeditor.fields import RichTextField

from .managers import APIGuideManager
from .utils import get_image_name


import os

PING_URL = 'https://www.google.com/webmasters/tools/ping'

class SiteInfo(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(null=True,blank=True)
    main_content  = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to=get_image_name,blank=True,null=True)
    portfolio_url = models.URLField(blank=True,null=True)


    def __str__(self):
        return self.title 
    
    def safe_about_content(self):
        return mark_safe(self.main_content)
    
    def validated_image_url(self):
        try:
            image_url = self.image.url
        except:
            image_url = None
        return image_url

class ApiGuide(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,blank=True,null=True)
    overview = models.TextField(blank=True,null=True)
    content = RichTextField()
    active = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order= models.PositiveIntegerField(default=1)

    objects = APIGuideManager()

    class Meta:
        ordering = ['-order','-timestamp']
        verbose_name = 'API Guide'
        verbose_name_plural = 'API Guides'

    def __str__(self):
        return self.name + ' API Guide '
    
    def safe_content(self):
        return mark_safe(self.content)
    
    def get_absolute_url(self):
        return reverse('main:detail',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        base_url = getattr(settings,'BASE_URL','findyourapi.com/')
        sitemap_path = os.path.join(base_url,'sitemap.xml')
        print(sitemap_path)
        try:
            ping_google(sitemap_url=sitemap_path,
                        ping_url=PING_URL,
                        sitemap_uses_https=False)
        except:
            print('some thing wrong')
            pass


class Suggestion(models.Model):
    name = models.CharField(max_length=255)
    email  = models.EmailField()
    subject = models.CharField(max_length=255)
    suggestion = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' Suggestion'


class Contact(models.Model):
    gmail = models.EmailField(null=True,blank=True)
    outlook = models.EmailField(null=True,blank=True)
    image = models.ImageField(upload_to=get_image_name,blank=True,null=True)
    
    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'
    def __str__(self):
        return self.gmail or self.outlook or 'Empty Email Fields'
    
    def validated_image_url(self):
        try:
            image_url = self.image.url
        except:
            image_url = None
        return image_url