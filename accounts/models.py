from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse

from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    username = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_shortname(self):
        return self.username

    def get_fullname(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    # def get_absolute_url(self):
    #     # return reverse('accounts:profile',kwargs={'user_slug':self.slug})


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='profile')

#     description = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user + ' profile'
