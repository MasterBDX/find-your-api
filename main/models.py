from django.db import models
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField

class ApiGuide(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,blank=True,null=True)
    content = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + ' api'
    
    def safe_content(self):
        return mark_safe(self.content)
