from django.contrib import admin

from .models import UserApiModel,PostApiModel,CommentApiModel

admin.site.register(UserApiModel)
admin.site.register(PostApiModel)
admin.site.register(CommentApiModel)