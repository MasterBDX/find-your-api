from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


GENDER = [('male','Male'),('female','Female')]

class UserApiModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    username = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=GENDER)
    birthday = models.DateField()
    birth_place = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(default='+12125552368')
    address = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name  = 'User'
        verbose_name_plural = 'Users Api'

    def __str__(self):
        return self.username


class PostApiModel(models.Model):
    author_id = models.PositiveIntegerField(default=1)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    title = models.CharField(max_length=255)
    overview = models.TextField()
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts Api'

    def __str__(self):
        return self.title
     
     
class CommentApiModel(models.Model):
    user_id  =  models.PositiveIntegerField(default=1)
    username = models.CharField(max_length=255,default='username')
    email = models.EmailField(default='email@mail.com')
    post_id = models.PositiveIntegerField(default=1)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments Api'

    def __str__(self):
        return self.user_id.username + ' comment' 