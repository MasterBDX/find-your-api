from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .utils import get_thumnail_name

GENDER = [('male','Male'),('female','Female')]

class UserApiModel(models.Model):
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    username = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=255,choices=GENDER)
    birthday = models.DateField()
    birth_place = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name  = 'User Api'
        verbose_name_plural = 'Users Api'

    def __str__(self):
        return self.username


class PostApiModel(models.Model):
    author = models.ForeignKey(UserApiModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=get_thumnail_name)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
     
