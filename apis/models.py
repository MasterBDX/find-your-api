from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.timezone import now
from .global_utils import get_thumnail_name

GENDER = [('male','Male'),('female','Female')]

class UserApiModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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
        verbose_name  = 'User'
        verbose_name_plural = 'Users Api'

    def __str__(self):
        return self.username


class PostApiModel(models.Model):
    author_id = models.ForeignKey(UserApiModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=get_thumnail_name,blank=True,null=True)
    published_at = models.DateField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts Api'

    def __str__(self):
        return self.title
     
     
class CommentApiModel(models.Model):
    user_id = models.ForeignKey(UserApiModel,
                                related_name='comments',
                                on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostApiModel,
                                related_name='comments',
                                verbose_name="posts",
                                on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments Api'

    def __str__(self):
        return self.user_id.username + ' comment' 