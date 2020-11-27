from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse


from ckeditor.fields import RichTextField

from .utils import get_image_name

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
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + ' API Guide '
    
    def safe_content(self):
        return mark_safe(self.content)
    
    def get_absolute_url(self):
        return reverse('main:detail',kwargs={'slug':self.slug})


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