from django.contrib import admin

from .models import UserApiModel,PostApiModel

admin.site.register(UserApiModel)
admin.site.register(PostApiModel)